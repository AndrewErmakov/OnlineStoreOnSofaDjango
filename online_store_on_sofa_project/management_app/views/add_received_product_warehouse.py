from django.shortcuts import redirect, render
from django.views import View

from rolepermissions.mixins import HasPermissionsMixin

from store_app.models import Product, Warehouse


class AddReceivedProductToWarehouse(View, HasPermissionsMixin):
    required_permission = 'change_info_existing_products'

    def get(self, request, pk):
        try:
            return render(request=request,
                          template_name='add_count_received_product_to_warehouse.html',
                          context={'product': Product.objects.get(pk=pk)})
        except Exception as e:
            print(e)
            return redirect('home')

    def post(self, request, pk):
        try:
            product_in_warehouse = Warehouse.objects.get(product=Product.objects.get(pk=pk))
            product_in_warehouse.quantity += int(request.POST.get('count_prod'))
            product_in_warehouse.save()

            return redirect('change_info_product')
        except Exception as e:
            print(e)
            return redirect('home')
