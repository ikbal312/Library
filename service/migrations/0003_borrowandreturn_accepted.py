# Generated by Django 4.2.4 on 2023-08-31 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowandreturn',
            name='accepted',
            field=models.BooleanField(default=0),
        ),
    ]
