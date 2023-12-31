# Generated by Django 4.2.4 on 2023-09-05 15:31

import book.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0003_bookimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='creation_date',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='creator',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=book.models.upload_to),
        ),
        migrations.DeleteModel(
            name='BookImage',
        ),
    ]
