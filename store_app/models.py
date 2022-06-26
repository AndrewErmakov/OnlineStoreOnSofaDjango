from django.contrib.auth.models import User
from django.core import validators
from django.db import models


class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']

    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name='Название рубрики',
        validators=[validators.MinLengthValidator(3)],
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        db_table = 'product'
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-sale_start_time']

    name = models.CharField(
        max_length=50,
        verbose_name='Название товара',
        validators=[validators.MinLengthValidator(5)],
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
        validators=[validators.MinLengthValidator(15)],
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        blank=True, null=True,
        verbose_name='Цена',
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(1000000),
        ],
    )
    brand = models.CharField(
        max_length=50,
        verbose_name='Бренд',
        validators=[validators.MinLengthValidator(2)],
    )
    sale_start_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата начала продажи',
    )
    avg_rating = models.DecimalField(
        max_digits=3, decimal_places=2,
        blank=True, null=True,
        verbose_name='Рейтинг товара',
        default=None,
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(5),
        ],
    )

    category = models.ForeignKey(
        to='Category',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Рубрика',
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Комментарий к товару"""

    class Meta:
        db_table = 'comment'
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['product']

    text = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    rating = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(5),
        ],
        verbose_name='Оценка',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата комментирования',
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='Товар',
        related_name='comments',
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='comments',
    )

    def __str__(self):
        return self.product.name


class ImageProduct(models.Model):
    """Изображение товара"""

    class Meta:
        db_table = 'image_product'
        verbose_name_plural = 'Изображения товаров'
        verbose_name = 'Изображение товара'
        ordering = ['product']

    image = models.ImageField(
        null=True, blank=True,
        verbose_name='Изображения товара',
        upload_to="images/store_app/products/",
        validators=[validators.validate_image_file_extension],
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    class Meta:
        db_table = 'cart'
        verbose_name_plural = 'Корзина пользователя с товарами'
        verbose_name = 'Товар в корзине'
        ordering = ['user']

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Никнейм покупателя',
    )
    products = models.ManyToManyField(Product, verbose_name='Товары в корзине')

    def __str__(self):
        return 'Корзина пользователя с товарами ' + self.user.username


class ProductInCart(models.Model):
    """Товар в корзине"""

    class Meta:
        db_table = 'product_in_cart'
        verbose_name_plural = 'Количество определенного товара в корзине'
        ordering = ['cart']

    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество данного товара')

    cart = models.ForeignKey(
        to=Cart,
        on_delete=models.CASCADE,
        verbose_name='Корзина',
        blank=True,
        null=True,
        related_name='product_in_cart',
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='Название товара',
    )

    def __str__(self):
        return f'В корзине {self.cart.user.username} ' \
               f'лежит товар {self.product.name} в количестве ' \
               f'{self.quantity}'


class Warehouse(models.Model):
    """Склад товаров"""

    class Meta:
        db_table = 'warehouse'
        verbose_name_plural = 'Склад товаров'
        verbose_name = 'Ячейка для хранения одной позиции товара'
        ordering = ['product']

    quantity = models.PositiveSmallIntegerField(verbose_name='Количество товаров')

    product = models.OneToOneField(
        to=Product,
        on_delete=models.DO_NOTHING,
        verbose_name='Товар',
    )

    def __str__(self):
        return self.product.name + ' с количеством ' + str(self.quantity)


class Recipient(models.Model):
    """Получатель заказа"""

    class Meta:
        db_table = 'recipient'
        verbose_name_plural = 'Получатели заказа'
        verbose_name = 'Получатель заказа'
        ordering = ['name', 'surname']

    name = models.CharField(
        max_length=50,
        verbose_name='Имя получателя заказа',
        blank=True, null=True,
    )
    surname = models.CharField(
        max_length=50,
        verbose_name='Фамилия получателя заказа',
        blank=True, null=True,
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Номер телефона получателя заказа',
        blank=True, null=True,
    )

    def __str__(self):
        return f'{self.name} {self.surname}'


class Order(models.Model):
    """Оформленный заказ"""

    class Meta:
        db_table = 'order'
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['num_order', 'created_at']

    num_order = models.CharField(
        max_length=20,
        verbose_name='Номер заказа',
        blank=True, null=True,
        unique=True,
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время создания зказа',
        db_index=True,
    )

    buyer_email = models.EmailField(verbose_name='Электронная почта покупателя')

    total_price = models.DecimalField(
        max_digits=9, decimal_places=2,
        blank=True, null=True,
        verbose_name='Итоговая цена заказа',
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(1000000),
        ],
    )
    payment_method = models.CharField(max_length=30, verbose_name='Способ оплаты')
    method_receive_order = models.CharField(
        max_length=30,
        verbose_name='Способ получения заказа',
        default='Самовывоз',
    )

    date_order = models.DateField(
        db_index=True,
        verbose_name='Дата получения заказа',
        blank=True, null=True,
    )

    recipient = models.ForeignKey(
        to=Recipient,
        on_delete=models.CASCADE,
        verbose_name='Получатель',
    )


class OrderProduct(models.Model):
    """Товар в заказе"""

    class Meta:
        db_table = 'order_product'
        verbose_name_plural = 'Товары в заказах'
        verbose_name = 'Товар в заказе'
        ordering = ['product', 'quantity']

    quantity = models.PositiveIntegerField(verbose_name='Количество данного товара')

    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ',
        null=True, blank=True,
        related_name='product_in_order',
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='Название товара',
        related_name='product_in_order',
    )

    def __str__(self):
        return f'Заказ №{str(Order.num_order).zfill(6)}.'


class ClientFeedback(models.Model):
    """Обращение клиентов с просьбой об обратной связи"""

    class Meta:
        db_table = 'client_feedback'
        verbose_name_plural = 'Заявки на обратную связь'
        verbose_name = 'Заявка на обратную связь'
        ordering = ['name', 'phone', 'email', 'given_feedback']

    name = models.CharField(
        max_length=50,
        verbose_name='Имя клиента',
        validators=[validators.MinLengthValidator(5)],
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Номер телефона для обратной связи',
    )
    email = models.EmailField(
        verbose_name='Электронная почта для обратной связи',
        validators=[validators.MinLengthValidator(5)],
    )

    question = models.TextField(
        verbose_name='Вопрос клиента',
        validators=[validators.MinLengthValidator(15)],
    )
    given_feedback = models.BooleanField(
        verbose_name='Дана ли обратная связь?',
        default=False,
    )

    def __str__(self):
        return f'Заявка на обратную связь №{str(self.pk).zfill(6)}'
