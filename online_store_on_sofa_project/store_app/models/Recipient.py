from django.db import models


class Recipient(models.Model):
    """Модель получателя заказа"""
    name = models.CharField(max_length=50, verbose_name='Имя получателя заказа', blank=True, null=True)
    surname = models.CharField(max_length=50, verbose_name='Фамилия получателя заказа', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона получателя заказа', blank=True,
                             null=True)

    class Meta:
        db_table = 'recipient'
        verbose_name_plural = 'Получатели заказа'
        verbose_name = 'Получатель заказа'
        ordering = ['name', 'surname']

    def __str__(self):
        return f'{self.name} {self.surname}'
