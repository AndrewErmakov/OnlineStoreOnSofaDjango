from django.db import models

from .Product import Product


class Warehouse(models.Model):
    """Модель склада товаров"""
    product = models.OneToOneField(Product, on_delete=models.DO_NOTHING, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество товаров')

    class Meta:
        db_table = 'warehouse'
        verbose_name_plural = 'Склад товаров'
        verbose_name = 'Ячейка для хранения одной позиции товара'
        ordering = ['product']

    def __str__(self):
        return self.product.name + ' с количеством ' + str(self.quantity)
