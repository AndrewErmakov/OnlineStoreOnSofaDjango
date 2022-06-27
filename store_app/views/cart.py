from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from store_app.models import Cart


class CartView(LoginRequiredMixin, View):
    """Класс страницы просмотра корзины пользователя"""

    def get(self, request):
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            products_in_cart = cart.product_in_cart.all()
            count_each_product = {}
            total_sum = 0

            for product_in_cart in products_in_cart:
                count_each_product[product_in_cart.product_id] = [
                    product_in_cart.quantity,
                    product_in_cart.quantity * product_in_cart.product.price,
                ]
                total_sum += product_in_cart.quantity * product_in_cart.product.price

            context = {
                'products': cart.products.all(),
                'is_empty_cart': False,
                'count_each_product': count_each_product,
                'total_sum': total_sum,
            }
        else:
            context = {'is_empty_cart': True}
        return render(
            request=request,
            template_name='user_cart_page.html',
            context=context,
        )
