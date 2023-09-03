from datetime import  timedelta
from rest_framework import serializers, exceptions
from .models import Borrow, Return, Wishlist, Notification, Reminder, Reservation



class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ['book', "duration"]


class ReturnSerializer(serializers.SerializerMethodField):
    class Meta:
        model = Return
        fields = ('id', 'title', 'fine')


class ReminderSerializer(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField(read_only=True)
    last_date = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Reminder
        fields = ["book_title", "borrowed_at", "last_date", 'fine']

    def get_last_date(self, obj):
        return obj.borrowed_at + timedelta(days=obj.duration)

    def get_book_title(self, obj):
        return obj.book.title


class WishlistListSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True)
    author = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Wishlist
        fields = ('id', 'title', 'author', 'status')

    def get_id(self, obj):
        return str(obj.book.id)

    def get_title(self, obj):
        return str(obj.book.title)

    def get_author(self, obj):
        return str(obj.book.author)

    def get_status(self, obj):
        return str(obj.book.status)


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ('book',)


class NotificationSerializer(WishlistListSerializer):
    class Meta(WishlistListSerializer.Meta):
        model = Notification
        depth =3

from .constants import WISH,RESERVATION
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('book',)


    def validate_book(self, book):
        if book.stock != 0:
            raise exceptions.ValidationError('Invalid stock')
        return book