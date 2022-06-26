from django.contrib.auth import views as auth_views
from django.urls import path

from .views import ActivateAccountView, ChangePasswordView, LoginView, \
    LogoutView, ResetPasswordView, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate_account/', ActivateAccountView.as_view(), name='activate_account'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),

    # urls of reset password
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
]
