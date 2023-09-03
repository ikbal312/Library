from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from .models import Book

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)

book_viewSet = BookViewSet





