
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), primary_key=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    is_admin = models.BooleanField(
        _("Admin status"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "

        ),
    )

    def __str__(self):
        return self.email



