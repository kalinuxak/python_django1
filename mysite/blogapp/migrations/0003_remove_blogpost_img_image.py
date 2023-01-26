# Generated by Django 4.1.5 on 2023-01-25 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blogpost_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='img',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='files/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.blogpost', verbose_name='Пост')),
            ],
        ),
    ]