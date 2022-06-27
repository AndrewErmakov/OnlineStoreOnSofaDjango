import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import RegistrationConfirmationByEmail


class LoginTestCase(TestCase):
    def setUp(self) -> None:
        self.user_data = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'password': 'password',
        }
        self.user: User = User.objects.create_user(**self.user_data)
        RegistrationConfirmationByEmail.objects.create(
            user=self.user,
            is_confirmed=True,
            activation_code='2345678903287363456',
        )

    def test_can_access_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login(self):
        response = self.client.post(
            reverse('login'),
            json.dumps(self.user_data),
            content_type='application/json',
        )
        user = User.objects.get(username=self.user_data['username'])

        self.assertTrue(user.is_authenticated)
        self.assertTrue(user.is_active)
        self.assertTemplateUsed(response, 'login.html')
