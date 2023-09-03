from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from book.permissions import BookAccessPermission
from .serializers import BookSerializer
from .models import Book


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    permission_classes = [BookAccessPermission]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

book_viewSet = BookViewSet







