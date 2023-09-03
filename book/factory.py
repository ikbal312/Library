
import factory
from factory.django import DjangoModelFactory
from .models import Book
class BookFactory(DjangoModelFactory):
    title = factory.Faker('sentence', nb_words= 15)
    isbn = factory.Faker('isbn13')
    author =factory.Faker('first_name',)
    genre = factory.Faker('name')
    stock = 7
    publication_date = factory.Faker('date')

    class Meta:
        model = Book

