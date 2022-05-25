from django.shortcuts import render, redirect
from django.views import View
from rolepermissions.mixins import HasPermissionsMixin
from store_app.models import Product


class ChangeProductInfoView(View, HasPermissionsMixin):
    required_permission = 'change_info_existing_products'

    def get(self, request):
        try:
            return render(request, 'change_info_existing_products.html', {'products': Product.objects.all()})
        except Exception as e:
            print(e)
            return redirect('home')

