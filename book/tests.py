import json

from rest_framework.test import APITestCase
from django.urls import reverse
from .factory import BookFactory

class TestBookAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("book-list")
        self.book = BookFactory()

    def test_get(self):
        response = self.client.get(self.url)
        response.render()
        self.assertEquals(200, response.status_code)
        expected_content = [{
            "id": str(self.book.id),
            "title": self.book.title,
            "author": self.book.author,
            "isbn": self.book.isbn,
            "stock": self.book.stock,
            "genre":self.book.genre,
            "publication_date": self.book.publication_date,
            "status": self.book.status
        }]

        self.assertListEqual(expected_content,
                            json.loads(response.content))