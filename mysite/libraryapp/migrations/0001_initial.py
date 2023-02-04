# Generated by Django 4.1.5 on 2023-02-04 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('birthday', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('ibsn', models.IntegerField(default=0)),
                ('pages', models.IntegerField(default=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 2, 4, 17, 35, 52, 310058))),
                ('author', models.ManyToManyField(related_name='books', to='libraryapp.author')),
            ],
        ),
    ]