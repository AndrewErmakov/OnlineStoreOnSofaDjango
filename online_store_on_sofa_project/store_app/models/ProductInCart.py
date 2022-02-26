from django.db import models

from .Product import Product
from .Cart import Cart


class ProductInCart(models.Model):
    """Модель одной позиции товара в корзине"""
    cart = models.ForeignKey(
        to=Cart,
        on_delete=models.CASCADE,
        verbose_name='Никнейм пользователя - владельца корзины',
        blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Название товара')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество данного товара')

    def __str__(self):
        return f'В корзине {self.cart.user.username} лежит товар {self.product.name} в количестве ' \
               f'{self.quantity}'

    class Meta:
        db_table = 'product_in_cart'
        verbose_name_plural = 'Количество определенного товара в корзине'
        ordering = ['cart']
