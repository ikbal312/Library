
import uuid
from django.db import models
from .manager import BookManager
from django.core.validators import RegexValidator

def upload_to(instance, filename):
    return f'books/{instance.title}-{instance.author}-{instance.isbn}-{instance.id}-{filename}'
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
                                )])
    author = models.CharField(max_length=12)
    genre = models.CharField(max_length=12)
    stock = models.PositiveIntegerField(editable=True,
                                        default=0)
    publication_date = models.DateField(editable=True,
                                        blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True, default='media/books/default.png')
    creator = models.ForeignKey('user.User', on_delete=models.SET_NULL, related_name='%(app_label)s_%(class)s_related',null=True)
    objects = BookManager()
    
    def __str__(self):
        return str(self.id)



    @property
    def status(self):
        if self.stock == 0:
            return 'unavailable'
        return 'available'
