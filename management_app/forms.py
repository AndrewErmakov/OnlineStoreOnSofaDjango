from django.forms import ModelForm

from store_app.models import ImageProduct, Product


class NewProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'brand', 'category']


class NewProductImageForm(ModelForm):
    class Meta:
        model = ImageProduct
        fields = ['image', 'product']
