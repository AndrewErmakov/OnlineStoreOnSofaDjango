from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import JsonResponse
from django.views import View

from store_app.models import Product, ProductInCart, Warehouse


class ReduceCountProductsView(LoginRequiredMixin, View):
    """Уменьшение числа одной позиции товара в корзине на 1"""

    def post(self, request):
        response_data = {}
        try:
            product = Product.objects.get(pk=request.POST.get('product_id'))

            product_in_cart = ProductInCart.objects.get(cart=request.user.cart, product=product)

            if product_in_cart.quantity == 1:
                response_data['status'] = 'ENOUGH'
                return JsonResponse(response_data)

            with transaction.atomic():
                product_in_cart.quantity -= 1
                product_in_cart.save()

                """Восполнение запасов на складе данной позициии товара"""
                product_in_warehouse = Warehouse.objects.get(product=product)
                product_in_warehouse.quantity += 1
                product_in_warehouse.save()

            response_data['status'] = 'OK'
            response_data['id'] = request.POST.get('product_id')
            response_data['price'] = product.price
            return JsonResponse(response_data)

        except Exception as e:
            print(e)
            response_data['status'] = 'BAD'
            return JsonResponse(response_data)
