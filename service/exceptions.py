from rest_framework import exceptions,status
from django.utils.translation import gettext_lazy as _
class InvalidBookStock(exceptions.ValidationError):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = _('Invalid input.')
    default_code = 'invalid'
