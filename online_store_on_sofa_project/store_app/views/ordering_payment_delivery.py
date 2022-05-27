from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect, render
from django.views import View

from store_app.accessory_modules import encryption_number_order
from store_app.models import Order, OrderProduct, ProductInCart, Recipient


class OrderingPaymentDeliveryView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'products': ProductInCart.objects.filter(cart__user=request.user),
            'user': request.user,
        }
        return render(
            request=request,
            template_name='ordering_payment_delivery.html',
            context=context,
        )

    def post(self, request):
        try:
            with transaction.atomic():
                recipient = Recipient.objects.create(
                    name=request.POST.get('name_recipient'),
                    surname=request.POST.get('surname_recipient'),
                    phone=request.POST.get('phone'),
                )
                order = Order.objects.create(
                    recipient=recipient,
                    buyer_email=request.user.email,
                    payment_method='При получении',
                )

                order.num_order = str(order.pk).zfill(6)

                """Находим корзину пользователя и товары в ней"""
                cart_user = request.user.cart
                total_sum = 0
                for product in cart_user.products.all():
                    product_in_cart = ProductInCart.objects.get(product=product, cart=cart_user)
                    total_sum += product_in_cart.quantity * product.price

                    """Теперь сохраним товары в таблицу БД ProductsInOrder"""
                    OrderProduct.objects.create(
                        order=order,
                        product=product,
                        quantity=product_in_cart.quantity,
                    )

                    """Удалим товар из таблицы ProductsInCart"""
                    product_in_cart.delete()

                order.total_price = total_sum
                order.save()

                """Очистим таблицу пользователя"""
                cart_user.delete()

                """Закодируем наш номер заказа и передадим ему в url страницы о создании заказа"""
                encrypt_num_order = encryption_number_order(order.pk)

            return redirect(
                to='order_created',
                encrypted_order_num=encrypt_num_order['encrypted_order_number'],
                key=encrypt_num_order['encryption_key'],
            )

        except Exception as e:
            print(e)
            return redirect('user_cart_page')
