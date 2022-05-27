from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from store_app.models import Cart, ProductInCart


class CartView(LoginRequiredMixin, View):
    """Класс страницы просмотра корзины пользователя"""

    def get(self, request):
        cart_user = Cart.objects.filter(user=request.user).first()
        if cart_user:
            products_in_cart = cart_user.products.all()
            count_each_product = {}
            total_sum = 0

            for product in products_in_cart:
                product_in_cart = ProductInCart.objects.filter(
                    cart=cart_user,
                    product=product,
                ).first()
                count_each_product[product.pk] = [product_in_cart.quantity]
                count_each_product[product.pk].append(product_in_cart.quantity * product.price)
                total_sum += product_in_cart.quantity * product.price

            context = {
                'products_in_cart': products_in_cart,
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

    def post(self, request):
        try:
            print(request.POST.get('payment_method_group'))
            return redirect('ordering_payment_' + request.POST.get('payment_method_group'))
        except Exception as e:
            print(e)
            return redirect('home')
