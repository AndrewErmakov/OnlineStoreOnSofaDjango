from django.db import models

from .Product import Product
from .Order import Order


class OrderProduct(models.Model):
    """Модель товаров в заказе"""
    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ',
        null=True, blank=True,
        related_name='product_in_order'
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='Название товара',
        related_name='product_in_order'
    )
    quantity = models.PositiveIntegerField(verbose_name='Количество данного товара')

    def __str__(self):
        return f'Заказ №{str(Order.num_order).zfill(6)}.'

    class Meta:
        db_table = 'order_product'
        verbose_name_plural = 'Товары в заказах'
        verbose_name = 'Товар в заказе'
        ordering = ['product', 'quantity']
