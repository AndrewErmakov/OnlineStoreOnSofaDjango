from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from store_app.models import Cart, ProductInCart


class CartView(View, LoginRequiredMixin):
    """Класс страницы просмотра корзины пользователя"""

    def get(self, request):
        try:
            cart_current_user = Cart.objects.filter(user=request.user).first()
            if cart_current_user:
                products_in_cart = cart_current_user.products.all()
                count_each_product = {}
                total_sum = 0
                for product in products_in_cart:
                    product_in_cart = ProductInCart.objects.filter(cart=cart_current_user, product=product).first()
                    count_each_product[product.pk] = [product_in_cart.quantity]
                    count_each_product[product.pk].append(product_in_cart.quantity * product.price)
                    total_sum += product_in_cart.quantity * product.price
                return render(request, 'user_cart_page.html', {'products_in_cart': products_in_cart,
                                                               'is_empty_cart': False,
                                                               'count_each_product': count_each_product,
                                                               'total_sum': total_sum})
            else:
                return render(request, 'user_cart_page.html', {'is_empty_cart': True})
        except Exception as e:
            print(e)
            return redirect('home')

    def post(self, request):
        try:
            print(request.POST.get('payment_method_group'))
            return redirect('ordering_payment_' + request.POST.get('payment_method_group'))
        except Exception as e:
            print(e)
            return redirect('home')
