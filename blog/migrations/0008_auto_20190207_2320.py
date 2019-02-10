# Generated by Django 2.1.5 on 2019-02-08 05:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190207_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='current_page',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(models.IntegerField())]),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(),
        ),
    ]