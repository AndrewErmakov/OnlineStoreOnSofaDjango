# Generated by Django 3.1.3 on 2022-02-26 18:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store_app', '0036_auto_20220224_1701'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartUser',
            new_name='Cart',
        ),
        migrations.RenameModel(
            old_name='Rubric',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author_comment',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date_comment',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='text_comment',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='total_sum',
            new_name='total_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='rubric',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='recipient',
            table='recipient',
        ),
    ]