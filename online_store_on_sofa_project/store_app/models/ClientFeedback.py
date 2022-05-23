from django.core import validators
from django.db import models


class ClientFeedback(models.Model):
    """Модель обращения клиентов с просьбой об обратной связи"""
    name = models.CharField(
        max_length=50,
        verbose_name='Имя клиента',
        validators=[validators.MinLengthValidator(5)]
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Номер телефона для обратной связи'
    )
    email = models.EmailField(
        verbose_name='Электронная почта для обратной связи',
        validators=[validators.MinLengthValidator(5)]
    )

    question = models.TextField(
        verbose_name='Вопрос клиента',
        validators=[validators.MinLengthValidator(15)],
    )
    given_feedback = models.BooleanField(verbose_name='Дана ли обратная связь?', default=False)

    def __str__(self):
        return f'Заявка на обратную связь №{str(self.pk).zfill(6)}'

    class Meta:
        db_table = 'client_feedback'
        verbose_name_plural = 'Заявки на обратную связь'
        verbose_name = 'Заявка на обратную связь'
        ordering = ['name', 'phone', 'email', 'given_feedback']
