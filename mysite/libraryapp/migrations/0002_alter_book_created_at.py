# Generated by Django 4.1.5 on 2023-07-29 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 29, 13, 29, 42, 725063)),
        ),
    ]
