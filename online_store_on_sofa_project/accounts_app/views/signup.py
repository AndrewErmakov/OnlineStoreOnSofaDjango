import random
import string

from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render
from django.views import View

from ..forms import RegisterForm
from ..models import RegistrationConfirmationByEmail
from ..tasks import send_letter_confirm_registration


class SignUpView(View):
    """
    New User Registration
    """

    def get(self, request):
        if request.user.is_anonymous:
            return render(
                request=request,
                template_name='signup.html',
                context={'form': RegisterForm()},
            )
        else:
            return redirect('home')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password1 = form.cleaned_data['repeat_password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            if password == password1:
                with transaction.atomic():
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                    )

                    secret_code = self.generate_secret_code()
                    self.save_registration_attempt(user=user, code=secret_code)

                    data = {
                        'email': email,
                        'first_name': first_name,
                        'last_name': last_name,
                        'code': secret_code,
                    }
                    send_letter_confirm_registration.delay(data)

                return redirect('activate_account')
            else:
                return self.get(request)

    @staticmethod
    def generate_secret_code():
        return ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
            for _ in range(30)
        )

    @staticmethod
    def save_registration_attempt(user, code):
        registration_attempt = RegistrationConfirmationByEmail()
        registration_attempt.user = user
        registration_attempt.activation_code = code
        registration_attempt.save()
