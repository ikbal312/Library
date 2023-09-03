from django.forms import models
from .models import User


class UserSignUpForm(models.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')


class UserSignInForm(models.ModelForm):
    class Meta:
        models = User
        fields = ('email', 'password')
