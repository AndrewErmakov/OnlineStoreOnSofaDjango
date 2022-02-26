from django.contrib.auth.models import User
from django.core import validators
from django.db import models

from .Product import Product


class Comment(models.Model):
    """Модель комментария к товару"""
    text = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    rating = models.PositiveSmallIntegerField(validators=[validators.MaxValueValidator(5)], verbose_name='Оценка')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата комментирования')

    class Meta:
        db_table = 'comment'
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['product']

    def __str__(self):
        return self.product.name


