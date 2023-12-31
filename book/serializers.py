from rest_framework import serializers
from .models import Book


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','image']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'isbn', 'publication_date', 'genre', 'stock', 'status','image')
