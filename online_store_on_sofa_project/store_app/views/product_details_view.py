from django.shortcuts import render
from django.views import View

from store_app.models import Product, Category, Warehouse


class ProductDetailsView(View):
    """Класс просмотра страницы - подробности о выбранном товаре"""

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        rubrics = Category.objects.all()

        try:
            count_product_in_warehouse = Warehouse.objects.get(product=product).quantity
        except Exception as e:
            print(e)
            count_product_in_warehouse = 0

        try:
            presence_flag_comment_user = bool(len(product.comments.filter(author_comment=request.user)))
        except Exception as e:
            print(e)
            presence_flag_comment_user = False

        context = {
            'product': product,
            'rubrics': rubrics,
            'presence_flag_comment_user': presence_flag_comment_user,
            'rating': (0, product.avg_rating)[product.avg_rating >= 0],
            'count_product': count_product_in_warehouse
        }
        return render(request, 'product_details.html', context)
