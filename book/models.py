
import uuid
from django.db import models
from .manager import BookManager, AuthorManager, GenreManager
from django.core.validators import RegexValidator


class Book(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=125,
                             editable=True,
                             null=False,
                             blank=False)
    isbn = models.TextField(max_length=13,
                            validators=[
                                RegexValidator(
                                    regex=r"^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$",
                                    message='10 or 13 digit isbn number required',
                                    code='invalid_ISBN'
                                )
                            ])
    author = models.CharField(max_length=12)
    genre = models.CharField(max_length=12)
    stock = models.PositiveIntegerField(editable=True,
                                        default=0)
    publication_date = models.DateField(editable=True,
                                        blank=False)

    objects = BookManager()
    @property
    def status(self):
        if self.stock == 0:
            return 'unavailable'
        return 'available'


    def __str__(self):
        return str(self.id)



