from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View

from accounts_app.tasks import send_letter_reset_password


class ResetPasswordView(View):
    """
    Класс страницы сброса пароля, если пользователь забыл его
    """

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            context = {'form': PasswordResetForm()}
            if kwargs:
                context.update(kwargs)
            return render(request, 'password_reset.html', context)
        else:
            redirect('home')

    def post(self, request):

        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email']).first()
            if user:
                try:
                    main_info = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Online store on sofa TOP SHOP',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": f'{user.first_name} {user.last_name}',
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    send_letter_reset_password.delay(main_info, user.email)
                    return redirect('password_reset_done')
                except Exception as e:
                    return self.get(request, error=e)
            else:
                error = f'Пользователя с электронной почтой {form.cleaned_data["email"]} нет в базе данных'
            return self.get(request, error=error)

