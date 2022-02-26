from django.shortcuts import render
from django.views import View
from django.db.models import Q

from store_app.models import Product, Category

SORT_MAPPER = {
    'price_asc': ('price', 'по возрастанию цены'),
    'price_desc': ('-price', 'по убыванию цены'),
    'top_rating': ('-avg_rating', 'по рейтингу'),
    'many_reviews': ('-count_reviews', 'по количеству отзывов'),
}


class ProductListView(View):
    """Класс просмотра домашней страницы: на ней отображаются товары-новинки"""

    def get(self, request):
        context = {}
        query_params = request.GET

        products = Product.objects.all()
        rubrics = Category.objects.all()

        rubric_id = query_params.get('rubric')
        if rubric_id is not None:
            rubric = rubrics.get(id=int(rubric_id))
            products = products.filter(rubric=rubric)
            context['rubric'] = rubric.name

        sorting_type = query_params.get('sort_by')
        if sorting_type is not None:
            products = products.order_by(SORT_MAPPER[sorting_type][0])
            context['sorting_type'] = SORT_MAPPER[sorting_type][1]

        chars2search = query_params.get('search')
        if chars2search:
            products = products.filter(
                Q(title__icontains=chars2search) |
                Q(description__icontains=chars2search) |
                Q(brand__icontains=chars2search)
            )
            context['search_text'] = chars2search

        context['new_products'], context['rubrics'] = products, rubrics
        return render(request, 'home.html', context)
