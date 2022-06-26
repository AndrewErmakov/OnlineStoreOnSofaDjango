from django.core.mail import send_mail

from config.celery import app


@app.task
def give_feedback(feedback_id: str,
                  message: str,
                  from_email: str,
                  to_email: str):
    send_mail(
        subject=f'Заявка на обратную связь №{feedback_id}',
        message=message,
        from_email=from_email,
        recipient_list=[to_email],
    )
