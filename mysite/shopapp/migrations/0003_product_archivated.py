# Generated by Django 4.1.5 on 2023-01-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_product_created_at_product_discount_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='archivated',
            field=models.BooleanField(default=False),
        ),
    ]
