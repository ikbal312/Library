from datetime import date
from django.db import models
from .constants import REMINDER_DAYS,RESERVATION
from django.db import transaction
class BorrowRequestManager(models.Manager):
    def confirm_request(self):
        pass

class ReminderManager(models.Manager):

    def get_reminders(self, queryset):
        _borrowQ = queryset
        _ids = []
        for _Q in _borrowQ:
            _duration = _Q.duration
            _borrowed_at = _Q.borrowed_at
            _today = date.today()
            if _duration - (_today - _borrowed_at).days <= REMINDER_DAYS:
                _ids.append(str(_Q.id))
        return _borrowQ.select_related().filter(id__in=_ids)


class ReturnManager(models.Manager):
    pass


class WishlistManager(models.Manager):
   pass



class NotificationManager(models.Manager):
    def get_notification(self, queryset):
        wQ = queryset.filter(type=RESERVATION)
        l =[q for q in wQ if q.book.stock > 0]
        return l


class ReservationManager(models.Manager):
    pass