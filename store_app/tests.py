from config.utils import reverse_with_query_params

from django.test import TestCase
from django.urls import reverse

from .models import Category, Product


class ProductListTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        for category in ('category1', 'category2', 'category3'):
            Category.objects.create(name=category)

        product_quantity = 21
        brands = (
            'abibas', 'ruma', 'greebok', 'musa', 'lakey', 'ucrop',
        )
        for i in range(product_quantity):
            Product.objects.create(
                name=f'Товар №{i + 10}',
                description=f'Описание {i + 10}',
                price=i + 100,
                brand=brands[i % len(brands)],
                category_id=i % 3 + 1,
            )

    def test_product_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

        self.__check_categories(response)

        paginator = response.context['page_obj']
        self.assertEqual(paginator.number, 1)
        products = paginator.object_list

        self.assertEqual(len(products), 6)

        for product in products:
            self.assertIn(product.id, range(16, 22))

        product = products[0]
        self.assertEqual(product.id, 21)
        self.assertEqual(product.name, 'Товар №30')
        self.assertEqual(product.description, 'Описание 30')
        self.assertEqual(product.price, 120)

        self.assertTrue(paginator.has_next())
        self.assertEqual(paginator.next_page_number(), 2)

    def test_product_list_filter_by_category(self):
        response = self.client.get(reverse_with_query_params(
            view='home',
            query_kwargs={'category': 1},
        ))
        self.assertEqual(response.status_code, 200)

        self.__check_categories(response)

        paginator = response.context['page_obj']
        self.assertEqual(paginator.number, 1)
        products = paginator.object_list

        self.assertEqual(len(products), 6)

        for product in products:
            self.assertEqual(product.category_id, 1)
            self.assertNotIn(product.category_id, (2, 3))

        product = products[0]
        self.assertEqual(product.id, 19)
        self.assertEqual(product.name, 'Товар №28')
        self.assertEqual(product.description, 'Описание 28')
        self.assertEqual(product.price, 118)

        self.assertTrue(paginator.has_next())
        self.assertEqual(paginator.next_page_number(), 2)

    def test_search_product_list(self):
        response = self.client.get(reverse_with_query_params(
            view='home',
            query_kwargs={'search': 'Товар №3'},
        ))
        self.assertEqual(response.status_code, 200)

        self.__check_categories(response)

        paginator = response.context['page_obj']
        self.assertEqual(paginator.number, 1)
        products = paginator.object_list

        self.assertEqual(len(products), 1)

        product = products[0]

        self.assertEqual(product.id, 21)
        self.assertEqual(product.name, 'Товар №30')
        self.assertEqual(product.category_id, 3)

        self.assertFalse(paginator.has_next())

    def __check_categories(self, response):
        categories = response.context['categories']
        self.assertEqual(len(categories), 3)
        for category in categories:
            self.assertIn(category.name, ('category1', 'category2', 'category3'))
            self.assertIn(category.id, (1, 2, 3))
