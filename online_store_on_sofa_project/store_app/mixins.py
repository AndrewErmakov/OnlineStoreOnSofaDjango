from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect

from store_app.models import Order


class CheckOrderDetailMixin(AccessMixin):
    """
        Проверка, что пользователь прошел по ссылке, на которой содержатся
        детали созданного им заказа
    """

    def dispatch(self, request, *args, **kwargs):
        encrypted_order_num = kwargs.get('encrypted_order_num')
        key = kwargs.get('key')

        if not isinstance(encrypted_order_num, int) or not isinstance(key, int):
            permission_flag = False
        else:
            order = Order.objects.filter(id=encrypted_order_num - key).first()
            permission_flag = True if order and self.__check_buyer(order, request.user) else False

        if not request.user.is_authenticated or not permission_flag:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def __check_buyer(order: Order, user: User) -> bool:
        return order.buyer_email == user.email
