from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import JsonResponse
from django.views import View

from store_app.models import Product, ProductInCart, Warehouse


class IncreaseCountProductsView(LoginRequiredMixin, View):
    """
        Увеличение числа одной позиции товара в корзине на 1
    """

    def post(self, request):
        response_data = {}
        try:
            product = Product.objects.get(pk=request.POST.get('product_id'))

            product_in_cart = ProductInCart.objects.get(cart=request.user.cart,
                                                        product=product)

            """Проверка наличия еще 1 экземпляра товара"""
            product_in_warehouse = Warehouse.objects.get(product=product)
            if product_in_warehouse.quantity >= 1:
                with transaction.atomic():
                    """Товар на складе есть"""
                    product_in_cart.quantity += 1
                    product_in_cart.save()

                    """Уменьшение запасов на складе данной позициии товара на 1"""
                    product_in_warehouse.quantity -= 1
                    product_in_warehouse.save()

                response_data['status'] = 'OK'
                response_data['id'] = request.POST.get('product_id')
                response_data['price'] = product.price
            else:
                """Товар на складе нет"""
                response_data['status'] = 'Not available'

            return JsonResponse(response_data)
        except Exception as e:
            print(e)
            response_data['status'] = 'BAD'
            return JsonResponse(response_data)
