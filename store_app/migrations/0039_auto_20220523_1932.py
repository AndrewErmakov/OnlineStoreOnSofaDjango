# Generated by Django 3.1.3 on 2022-05-23 19:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store_app', '0038_auto_20220226_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Имя клиента')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона для обратной связи')),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Электронная почта для обратной связи')),
                ('question', models.TextField(validators=[django.core.validators.MinLengthValidator(15)], verbose_name='Вопрос клиента')),
                ('given_feedback', models.BooleanField(default=False, verbose_name='Дана ли обратная связь?')),
            ],
            options={
                'verbose_name': 'Заявка на обратную связь',
                'verbose_name_plural': 'Заявки на обратную связь',
                'db_table': 'client_feedback',
                'ordering': ['name', 'phone', 'email', 'given_feedback'],
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество данного товара')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store_app.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.product', verbose_name='Название товара')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказах',
                'db_table': 'order_product',
                'ordering': ['product', 'quantity'],
            },
        ),
        migrations.DeleteModel(
            name='FeedBackWithClient',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='recipient',
            options={'ordering': ['name', 'surname'], 'verbose_name': 'Получатель заказа', 'verbose_name_plural': 'Получатели заказа'},
        ),
        migrations.RenameField(
            model_name='recipient',
            old_name='name_recipient',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='recipient',
            old_name='phone_recipient',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='recipient',
            old_name='surname_recipient',
            new_name='surname',
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='productincart',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_in_cart', to='store_app.cart', verbose_name='Корзина'),
        ),
        migrations.DeleteModel(
            name='ProductsInOrder',
        ),
    ]
