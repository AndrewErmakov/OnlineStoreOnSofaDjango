from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse
from django.views import View

from store_app.models import Cart, Product, ProductInCart, Warehouse


class AddProductToCartView(LoginRequiredMixin, View):
    """
        Добавление товара в корзину
    """

    def post(self, request):
        response_data = {}
        product = Product.objects.get(pk=request.POST.get('product_id'))

        try:
            product_in_warehouse = Warehouse.objects.get(product=product)
            """Проверка если пользователь ввел число, превышающее кол-во товара на складе,
            если превышает, то страница остается без изменений, в корзину ничего не добавляется"""
            if product_in_warehouse.quantity < int(request.POST.get('count_product')):
                response_data['status'] = 'MORE'
                return JsonResponse(response_data)

            cart = Cart.objects.filter(user=request.user).first()
            if cart:
                """Если корзина пользователя уже есть, и он добавлял ранее какой-то товар"""
                cart.products.add(product)
                try:
                    """
                    Если позиция данного товара уже в корзине и
                    пользователь еще хочет добавить несколько товаров одной позиции
                    """
                    product_in_cart = cart.product_in_cart.filter(product=product).first()
                    if not product_in_cart:
                        product_in_cart = ProductInCart.objects.create(
                            quantity=0,
                            product=product,
                            cart=cart,
                        )
                    product_in_cart.quantity += int(request.POST.get('count_product'))
                    product_in_cart.save()

                except Exception as e:
                    print(e)
                    """В существующую корзину добавляется новый товар и указывается количество"""
                    cart.product_in_cart.create(
                        product=product,
                        quantity=int(request.POST.get('count_product')),
                    )

            else:
                """Иначе создается корзина, и добавляется первый товар в корзину"""
                cart = Cart.objects.create(user=request.user)
                cart.products.add(product)
                ProductInCart.objects.create(
                    cart=cart,
                    product=product,
                    quantity=int(request.POST.get('count_product')),
                )

            """Кол-во этого товара теперь на складе уменьшается"""

            product_in_warehouse.quantity -= int(request.POST.get('count_product'))
            product_in_warehouse.save()

            response_data['status'] = 'OK'
            return JsonResponse(response_data)
        except Exception as e:
            print(e)
            print(request.user == AnonymousUser)
            response_data['status'] = 'BAD'
            return JsonResponse(response_data)
