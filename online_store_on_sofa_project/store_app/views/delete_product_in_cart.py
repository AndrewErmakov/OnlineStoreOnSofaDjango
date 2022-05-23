from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import JsonResponse
from django.views import View

from store_app.models import Product, ProductInCart, Cart, Warehouse


class DeleteProductInCartView(View, LoginRequiredMixin):
    """Удаление товара (только одной позиции!!!) из корзины"""

    def post(self, request):
        response_data = {}
        try:
            product = Product.objects.get(pk=request.POST.get('product_id'))

            with transaction.atomic():
                """Удаление товара из таблицы CartUser"""
                request.user.cart.products.remove(product)

                """Удаление из таблицы ProductInCart"""
                product_in_cart = ProductInCart.objects.get(cart=request.user.cart, product=product)
                quantity = product_in_cart.quantity
                product_in_cart.delete()

                """Восполнение запасов на складе данной позициии товара"""
                product_in_warehouse = Warehouse.objects.get(product=product)
                product_in_warehouse.quantity += quantity
                product_in_warehouse.save()

                if not request.user.cart.products.all().count():
                    request.user.cart.delete()

            response_data['status'] = 'OK'
            response_data['id'] = request.POST.get('product_id')
            return JsonResponse(response_data)

        except Exception as e:
            print(e)
            response_data['status'] = 'BAD'
            return JsonResponse(response_data)
