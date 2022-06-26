# Generated by Django 3.1.3 on 2020-11-07 16:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrationconfirmationbyemail',
            options={'verbose_name_plural': 'Подтверждения регистрации'},
        ),
        migrations.AddField(
            model_name='registrationconfirmationbyemail',
            name='activation_code',
            field=models.CharField(default='123456789009876543211234567890', max_length=30, validators=[django.core.validators.MinLengthValidator(30)]),
        ),
    ]