from rest_framework import mixins, exceptions,response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from .serializers import WishlistSerializer, WishlistListSerializer
from django.db import IntegrityError,transaction
from django.shortcuts import get_object_or_404
from .permissions import WishlistPermission

class WishlistViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = [WishlistPermission]
    def get_queryset(self):
        _user = self.request.user

        return _user.service_wishlist_related.all()
    def get_serializer_class(self):
        if self.request.method == "GET":
            return WishlistListSerializer
        return WishlistSerializer

    def get_object(self):
        queryset = self.get_queryset()
        book = self.kwargs['pk']
        obj = get_object_or_404(queryset, book=book)
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        _user = self.request.user
        try:
            serializer.save(user=_user)
        except IntegrityError:
            return response.Response(data={"error": "duplication Error"})