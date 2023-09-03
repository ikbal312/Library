from django.contrib.auth.models import UserManager as BaseManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseManager):
    """
    Custom user model manager where email is the unique identifiers for authentication
    """

    def create_user(self, email=None, password=None, **extra_fields):
        """
        create and save a user with give email and password
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        """
        create and save superuser with give email and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Super user must have is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Super user must have is_superuser=True"))
        return self.create_user(email=email, password=password, **extra_fields)
