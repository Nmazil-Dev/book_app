# Generated by Django 2.1.5 on 2019-02-10 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_book_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='owner',
        ),
    ]
