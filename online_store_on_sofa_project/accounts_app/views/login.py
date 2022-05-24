from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View

from accounts_app.forms import LoginForm
from accounts_app.models import RegistrationConfirmationByEmail


class LoginView(View):
    """
    Пользователь логинится на сайте, чтобы совершать дальнейшие покупки, если у него есть аккаунт,
    и пользователь подтвердил его с помощью электронной почты
    """

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            redirect('home')
        else:
            login_form = LoginForm()
            context = {'form': login_form}
            if kwargs:
                context.update(kwargs)
            return render(request, 'login.html', context)

    def post(self, request):
        error = None
        form = LoginForm(request.POST)
        if form.is_valid():

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('home')

                activation_state = RegistrationConfirmationByEmail.objects.filter(user=user).first()
                if activation_state is not None:
                    if activation_state.is_confirmed:
                        login(request, user)
                        return redirect('home')
                    else:
                        return redirect('activate_account')
            else:
                error = 'Введены неправильный логин и/или пароль'
        else:
            error = 'Возможно неправильно введены символы с капчи'
        return self.get(request, error=error)
