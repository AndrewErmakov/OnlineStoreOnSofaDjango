# Generated by Django 3.1.3 on 2021-01-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0023_auto_20210112_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата и время создания зказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateField(db_index=True, verbose_name='Дата получения заказа'),
        ),
    ]