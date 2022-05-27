from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class LoginTestCase(TestCase):
    def setUp(self) -> None:
        self.user = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'password': 'password',
        }
        user = User.objects.create_user(**self.user)
        user.is_active = True
        user.save()
        self.client = Client()

    def test_can_access_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
