from django.forms import ModelForm
from store_app.models import Product, ImageProduct


class NewProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'brand', 'category']


class NewProductImageForm(ModelForm):
    class Meta:
        model = ImageProduct
        fields = ['image', 'product']
