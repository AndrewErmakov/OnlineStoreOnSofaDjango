from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from store_app.accessory_modules import decryption_number_order


class CreatedOrderView(View, LoginRequiredMixin):
    """Класс просмотра страницы о созданном заказе"""

    def get(self, request, encrypted_order_num, key):
        try:
            return render(request, 'order_created.html',
                          {'num': decryption_number_order(encrypted_order_num, key)})
        except Exception as e:
            print(e)
            return redirect('home')
