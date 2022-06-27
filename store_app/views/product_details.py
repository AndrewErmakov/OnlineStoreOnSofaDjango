from django.shortcuts import render
from django.views import View

from store_app.models import Category, Product, Warehouse


class ProductDetailsView(View):
    """
        Детали товара
    """

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)

        product_in_warehouse = Warehouse.objects.filter(product=product).first()

        context = {
            'product': product,
            'categories': Category.objects.all(),
            'presence_flag_comment_user': product.comments.filter(author=request.user).count() > 0,
            'rating': product.avg_rating,
            'count_product': product_in_warehouse.quantity if product_in_warehouse else 0,
        }
        return render(
            request=request,
            template_name='product_details.html',
            context=context,
        )
