from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail, BadHeaderError
from django.template.loader import render_to_string

from online_store_on_sofa_project.celery import app


@app.task
def send_letter_confirm_registration(data: dict):
    """
        Отправка письма на почту, если пользователь регистрируется первый раз
    """
    template_name = 'confirmation_registration_email.html'
    html_body = render_to_string(template_name, data)
    msg = EmailMultiAlternatives(subject='Регистрация на сайте интернет-магазина TOP SHOP.', to=[data['email'], ])
    msg.attach_alternative(html_body, 'text/html')
    msg.send()


@app.task
def send_letter_reset_password(main_info, user_email):
    """
        Отправка письма на почту, если пользователю нужно сбросить пароль
    """

    email_template_letter = 'password_reset_email.html'
    email = render_to_string(email_template_letter, main_info)

    msg = EmailMultiAlternatives(subject='Запрос сброса пароля', to=[user_email, ])
    msg.attach_alternative(email, 'text/html')
    msg.send()
