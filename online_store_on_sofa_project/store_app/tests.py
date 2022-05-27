from django.test import TestCase
from django.urls import reverse

from store_app.models import Category, Product


class ProductListTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        for category in ('category1', 'category2', 'category3'):
            Category.objects.create(name=category)

        product_quantity = 20
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

        categories = response.context['categories']
        self.assertEqual(len(categories), 3)
        for category in categories:
            self.assertIn(category.name, ('category1', 'category2', 'category3'))
            self.assertIn(category.id, (1, 2, 3))

        paginator = response.context['page_obj']
        self.assertEqual(paginator.number, 1)
        products = paginator.object_list

        for product in products:
            self.assertIn(product.id, range(15, 21))

        product = products[0]
        self.assertEqual(product.id, 20)
        self.assertEqual(product.name, 'Товар №29')
        self.assertEqual(product.description, 'Описание 29')
        self.assertEqual(product.price, 119)

        self.assertTrue(paginator.has_next())
        self.assertEqual(paginator.next_page_number(), 2)
