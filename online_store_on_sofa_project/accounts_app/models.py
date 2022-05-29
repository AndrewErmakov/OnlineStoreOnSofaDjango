from django.contrib.auth.models import User
from django.core import validators
from django.db import models


class RegistrationConfirmationByEmail(models.Model):
    class Meta:
        db_table = 'registration_confirmation_by_email'
        verbose_name = 'Подтверждение регистрации'
        verbose_name_plural = 'Подтверждения регистрации'

    is_confirmed = models.BooleanField(default=False)
    activation_code = models.CharField(
        max_length=30,
        validators=[validators.MinLengthValidator(30)],
        default='123456789009876543211234567890',
    )
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    def __str__(self):
        return self.user.username
