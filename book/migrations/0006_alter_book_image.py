# Generated by Django 4.2.4 on 2023-09-05 17:59

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='media/books/default.png', null=True, upload_to=book.models.upload_to),
        ),
    ]
