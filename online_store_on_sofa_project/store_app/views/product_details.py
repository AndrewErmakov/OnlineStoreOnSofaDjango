from django.shortcuts import render
from django.views import View

from store_app.models import Product, Category, Warehouse


class ProductDetailsView(View):
    """Класс просмотра страницы - подробности о выбранном товаре"""

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)

        product_in_warehouse = Warehouse.objects.filter(product=product).first()

        context = {
            'product': product,
            'rubrics': Category.objects.all(),
            'presence_flag_comment_user': product.comments.filter(author=request.user).count() > 0,
            'rating': (0, product.avg_rating)[product.avg_rating >= 0],
            'count_product': product_in_warehouse.quantity if product_in_warehouse else 0,
        }
        return render(request, 'product_details.html', context)
