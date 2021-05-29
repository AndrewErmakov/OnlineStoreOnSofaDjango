# Generated by Django 3.1.3 on 2020-12-06 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0017_auto_20201206_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountProductsInCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_products_in_basket', models.PositiveIntegerField()),
                ('cart_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.cartuser')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.product')),
            ],
        ),
    ]