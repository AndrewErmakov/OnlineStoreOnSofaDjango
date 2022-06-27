from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect

from .models import Order


class CheckOrderDetailMixin(AccessMixin):
    """
        Проверка, что пользователь прошел по ссылке, на которой содержатся
        детали созданного им заказа
    """

    def dispatch(self, request, *args, **kwargs):
        filter_conditions = self.get_filter_conditions(kwargs)

        order = Order.objects.filter(**filter_conditions).first()
        permission_flag = bool(order and self.__check_buyer(order, request.user))

        if (not request.user.is_authenticated or not permission_flag) \
                and not request.user.is_superuser:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def get_filter_conditions(params: dict):
        filter_conditions = {
            key: params.get(key)
            for key in ('encrypted_order_num', 'key', 'num_order')
            if params.get(key)
        }

        if filter_conditions.keys() >= {'encrypted_order_num', 'key'}:
            encrypted_order_num = filter_conditions.pop('encrypted_order_num')
            key = filter_conditions.pop('key')
            filter_conditions['id'] = encrypted_order_num - key

        return filter_conditions

    @staticmethod
    def __check_buyer(order: Order, user: User) -> bool:
        return order.buyer_email == user.email
