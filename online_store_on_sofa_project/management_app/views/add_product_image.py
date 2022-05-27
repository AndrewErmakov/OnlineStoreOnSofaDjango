from django.shortcuts import redirect, render
from django.views import View

from rolepermissions.mixins import HasPermissionsMixin

from ..forms import NewProductImageForm


class AddProductImageView(View, HasPermissionsMixin):
    required_permission = 'add_images_for_product'

    def get(self, request):
        try:
            return render(
                request=request,
                template_name='add_images_for_product.html',
                context={'form': NewProductImageForm()},
            )
        except Exception as e:
            print(e)
            return redirect('home')

    def post(self, request):
        try:
            form = NewProductImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return redirect('add_images_for_product')

        except Exception as e:
            print(e)
            return redirect('home')
