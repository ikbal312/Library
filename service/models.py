import uuid
from datetime import date
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .manager import (BorrowRequestManager, WishlistManager, ReminderManager, NotificationManager, ReturnManager,
                      ReservationManager)
from .constants import RESERVATION, WISH, FINE_RATE


class BorrowAndReturn(models.Model):

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    book = models.ForeignKey(to='book.Book', related_name='%(app_label)s_%(class)s_related', on_delete=models.CASCADE)
    user = models.ForeignKey(to='user.User', related_name='%(app_label)s_%(class)s_related', on_delete=models.CASCADE)
    borrowed_at = models.DateField(default=date.today, editable=False)
    duration = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(limit_value=30),
            MinValueValidator(limit_value=1)
        ]
    )
    accepted = models.BooleanField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['book', 'user'], name='already borrowed')
        ]

    def __str__(self):
        return str(self.book)
    @property
    def fine(self):
        timedelta = date.today()-self.borrowed_at
        borrowed_duration = timedelta.days
        _duration = self.duration
        if borrowed_duration > _duration:
            due_days = borrowed_duration - _duration
            return FINE_RATE * due_days
        return 0


class Borrow(BorrowAndReturn):
    objects = BorrowRequestManager()
    class Meta:
        proxy = True


class Return(BorrowAndReturn):
    objects = ReturnManager()
    class Meta:
        proxy = True

class Wishlist(models.Model):
    TYPE = [
        (RESERVATION, 'Reservation'),
        (WISH, 'wish'),
    ]
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    book = models.ForeignKey(to='book.Book', related_name='%(app_label)s_%(class)s_related', on_delete=models.CASCADE)
    user = models.ForeignKey(to='user.User', related_name='%(app_label)s_%(class)s_related',on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE, default=WISH)
    objects = WishlistManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['book', 'user'], name='already in wishlist')
        ]

    def __str__(self):
        return str(self.book)


class Reminder(BorrowAndReturn):
    reminder = ReminderManager()

    class Meta:
        proxy = True




class Notification(Wishlist):
    class Meta:
        proxy = True
    notification = NotificationManager()


class Reservation(Wishlist):
    class Meta:
        proxy = True
    reservation = ReservationManager()