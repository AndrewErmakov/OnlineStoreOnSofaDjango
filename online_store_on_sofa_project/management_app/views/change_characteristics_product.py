from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.shortcuts import redirect, render
from django.views import View

from rolepermissions.mixins import HasPermissionsMixin

from store_app.models import Product


class ChangeCharacteristicsProductView(HasPermissionsMixin, View):
    required_permission = 'change_info_existing_products'

    def get(self, request, pk):
        try:
            return render(
                request=request,
                template_name='change_characteristics_product.html',
                context={'product': Product.objects.get(pk=pk)},
            )
        except PermissionDenied:
            return redirect('home')

    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)

            with transaction.atomic():
                product.name = request.POST.get('title')
                product.description = request.POST.get('description')
                product.price = request.POST.get('price')
                product.brand = request.POST.get('brand')
                product.save()

            return redirect('change_info_product')

        except PermissionDenied:
            return redirect('home')
