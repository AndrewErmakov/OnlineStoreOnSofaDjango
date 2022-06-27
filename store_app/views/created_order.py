from django.shortcuts import render
from django.views import View

from store_app.accessory_modules import decryption_number_order
from store_app.mixins import CheckOrderDetailMixin


class CreatedOrderView(CheckOrderDetailMixin, View):
    """
        Детали созданного заказа
    """

    def get(self, request, encrypted_order_num, key):
        return render(
            request=request,
            template_name='order_created.html',
            context={'num': decryption_number_order(encrypted_order_num, key)},
        )
