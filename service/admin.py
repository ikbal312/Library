from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    fields =('type',)
    list_display=('user','book_id','get_title')
    search_fields=('user__email',"book__id",)


    
    @admin.display(ordering='book__title',description='Book Title')
    def get_title(self,obj):
        return obj.book.title
