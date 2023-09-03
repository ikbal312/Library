from rest_framework import generics, exceptions, response, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import BorrowSerializer, ReturnSerializer, NotificationSerializer, ReminderSerializer, \
    ReservationSerializer
from django.db import transaction
from .permissions import ReservationPermisssion,NotificationPermission,BorrowPermission,ReminderPermission
from .constants import RESERVATION, WISH
from django.core.exceptions import ObjectDoesNotExist

class BorrowView(generics.CreateAPIView):
    serializer_class = BorrowSerializer
    permission_classes = [BorrowPermission]
    @transaction.atomic
    def perform_create(self, serializer):
        try:
            _user = self.request.user
            serializer.save(user=_user)
        except Exception:
            raise exceptions.ValidationError({'error': 'book exist'})


borrow_view = BorrowView.as_view()


class ReturnView(generics.UpdateAPIView):
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]


return_view = ReturnView.as_view()


class NotificationView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [NotificationPermission]

    @transaction.atomic
    def get_queryset(self):
        user = self.request.user
        model = self.get_serializer_class().Meta.model
        qs = user.service_wishlist_related.all()
        return model.notification.get_notification(queryset=qs)

notification_view = NotificationView.as_view()


class ReminderView(generics.ListAPIView):
    serializer_class = ReminderSerializer
    permission_classes = [ReminderPermission]

    @transaction.atomic
    def get_queryset(self):
        user = self.request.user
        qs = user.service_borrowandreturn_related.select_related().all()
        model = self.get_serializer_class().Meta.model
        return model.reminder.get_reminders(queryset=qs)


reminder_view = ReminderView.as_view()





class ReservationView(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes=[ReservationPermisssion]

    def get_queryset(self):
        return self.request.user.service_wishlist_related.select_related().all()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        user = self.request.user
        book = request.data['book']
        try:
            instance = self.get_queryset().get(book=book)
        except ObjectDoesNotExist:
            instance = None
        if (instance is not None) and instance.type == RESERVATION:
            return Response(data={"error": 'already reserved'}, status=status.HTTP_409_CONFLICT)
        if (instance is not None) and instance.type == WISH:
            instance.type = RESERVATION

        serializer = self.get_serializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        if instance is not None:
            serializer.save()
        else:
            serializer.save(user=user, type=RESERVATION)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

reservation_view = ReservationView.as_view()
