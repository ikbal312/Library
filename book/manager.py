from django.db import models
class BookManager(models.Manager):
    def search_title(self, title):
        return super().get_queryset().filter(title__icontain=title)

    def available(self, id):
        available = self.filter(id=id, stock__gt=0)
        if available:
            return True
        return False

    def decreaseStock(self, id):
        qs = super().get_queryset().get(id=id)
        qs.stock = qs.stock - 1
        qs.save()






