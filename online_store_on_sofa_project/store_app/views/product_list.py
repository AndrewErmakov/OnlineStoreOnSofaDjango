from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
    """Класс просмотра товаров"""

    def get(self, request):
        context = {}
        query_params = request.GET

        products = Product.objects.all()
        categories = Category.objects.all()

        category_id = query_params.get('category')
        if category_id is not None:
            category = categories.get(id=int(category_id))
            products = products.filter(category=category)
            context['category'] = category.name

        sorting_type = query_params.get('sort_by')
        if sorting_type is not None:
            products = products.order_by(SORT_MAPPER[sorting_type][0])
            context['sorting_type'] = SORT_MAPPER[sorting_type][1]

        chars2search = query_params.get('search')
        if chars2search:
            products = products.filter(
                Q(name__icontains=chars2search) |
                Q(description__icontains=chars2search) |
                Q(brand__icontains=chars2search)
            )
            context['search_text'] = chars2search

        page_number = query_params.get('page', 1)
        paginator = Paginator(products, 6)

        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)

        context['categories'], context['page_obj'] = categories, page_obj

        return render(request, 'home.html', context)
