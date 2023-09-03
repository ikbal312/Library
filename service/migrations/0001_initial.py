# Generated by Django 4.2.4 on 2023-08-31 06:04

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowAndReturn',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('borrowed_at', models.DateField(default=datetime.date.today, editable=False)),
                ('duration', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=30), django.core.validators.MinValueValidator(limit_value=1)])),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('RE', 'Reservation'), ('WI', 'wish')], default='WI', max_length=2)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='wishlist', to='book.book')),
            ],
            managers=[
                ('wishlistManager', django.db.models.manager.Manager()),
            ],
        ),
    ]