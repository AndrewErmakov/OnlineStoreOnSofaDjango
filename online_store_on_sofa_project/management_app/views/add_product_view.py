from django.shortcuts import render, redirect
from django.views import View
from rolepermissions.mixins import HasPermissionsMixin
from management_app.forms import NewProductForm
from store_app.models import Product, WarehouseProducts


class AddProductView(View, HasPermissionsMixin):
    required_permission = 'add_products'

    def get(self, request):
        try:
            form = NewProductForm()
            return render(request, 'add_new_products.html', {'form': form})
        except Exception as e:
            print(e)
            return redirect('home')

    def post(self, request):
        try:
            form = NewProductForm(request.POST)

            if form.is_valid():
                new_product = Product.objects.create(
                    title=form.cleaned_data['name'],
                    description=form.cleaned_data['description'],
                    price=form.cleaned_data['price'],
                    brand=form.cleaned_data['brand'],
                    rubric=form.cleaned_data['category']
                )
                WarehouseProducts.objects.create(
                    product=new_product,
                    count_products=request.POST.get('count_product')
                )
            return redirect('add_images_for_product')

        except Exception as e:
            print(e)
            return redirect('home')
