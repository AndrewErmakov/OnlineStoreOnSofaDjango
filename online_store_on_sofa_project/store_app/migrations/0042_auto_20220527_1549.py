# Generated by Django 3.1.3 on 2022-05-27 15:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0041_auto_20220527_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='avg_rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=-1, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Рейтинг товара'),
        ),
    ]
