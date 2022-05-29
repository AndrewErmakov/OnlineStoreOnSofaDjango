from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.shortcuts import redirect, render
from django.views import View

from rolepermissions.mixins import HasPermissionsMixin

from store_app.models import Product, Warehouse

from ..forms import NewProductForm


class AddProductView(HasPermissionsMixin, View):
    required_permission = 'add_products'

    def get(self, request):
        try:
            return render(
                request=request,
                template_name='add_new_products.html',
                context={'form': NewProductForm()},
            )
        except PermissionDenied:
            return redirect('home')

    def post(self, request):
        try:
            form = NewProductForm(request.POST)
            if form.is_valid():
                with transaction.atomic():
                    product = Product.objects.create(
                        name=form.cleaned_data['name'],
                        description=form.cleaned_data['description'],
                        price=form.cleaned_data['price'],
                        brand=form.cleaned_data['brand'],
                        category=form.cleaned_data['category'],
                    )
                    Warehouse.objects.create(
                        product=product,
                        quantity=request.POST.get('count_product', 0),
                    )
            return redirect('add_images_for_product')

        except PermissionDenied:
            return redirect('home')
