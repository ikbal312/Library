import factory
from factory.django import DjangoModelFactory
from ..models import User


class UserFactory(DjangoModelFactory):
    email = factory.Faker('email')
    first_name = factory.Faker('first_name'),
    last_name = factory.Faker('last_name'),
    class Meta:
        model = User

