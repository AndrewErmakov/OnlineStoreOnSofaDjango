# Generated by Django 3.1.3 on 2022-05-28 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0006_auto_20220527_1810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrationconfirmationbyemail',
            options={'verbose_name': 'Подтверждение регистрации', 'verbose_name_plural': 'Подтверждения регистрации'},
        ),
    ]
