from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from online_store_on_sofa_project.celery import app


@app.task
def send_letter_confirm_registration(data: dict):
    html_body = render_to_string('confirmation_registration_email.html', data)
    msg = EmailMultiAlternatives(subject='Регистрация на сайте интернет-магазина TOP SHOP.', to=[data['email'], ])
    msg.attach_alternative(html_body, 'text/html')
    msg.send()
