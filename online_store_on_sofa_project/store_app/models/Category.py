from django.core import validators
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name='Название рубрики',
        validators=[validators.MinLengthValidator(3)]
    )

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']

    def __str__(self):
        return self.name
