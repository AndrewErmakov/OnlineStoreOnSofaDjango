from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from store_app.models import Order


class HistoryOrdersView(View, LoginRequiredMixin):
    """Класс просмотра истории заказов"""

    def get(self, request):
        """Получение истории страницы заказов"""
        try:
            return render(
                request=request,
                template_name='order_history.html',
                context={'orders': Order.objects.filter(buyer_email=request.user.email)}
            )
        except Exception as e:
            print(e)
            return redirect('home')
