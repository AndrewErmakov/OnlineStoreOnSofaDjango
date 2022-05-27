from django.conf import settings
from django.db import transaction
from django.http import JsonResponse
from django.views import View

from rolepermissions.mixins import HasPermissionsMixin

from store_app.models import ClientFeedback

from ..tasks import give_feedback


class SendAnswerToClientFeedbackClaim(HasPermissionsMixin, View):
    required_permission = 'feedback_with_clients'

    def post(self, request):
        response_data = {}
        try:
            request_feedback_id = request.POST.get('request_feedback_id')
            text_answer = request.POST.get('text_answer')

            with transaction.atomic():
                feedback_request = ClientFeedback.objects.get(id=request_feedback_id)
                feedback_request.given_feedback = True
                feedback_request.save()

            response_data['status'] = 'OK'

            give_feedback.delay(
                feedback_id=request_feedback_id,
                message=text_answer,
                from_email=settings.EMAIL_HOST_USER,
                to_email=feedback_request.email,
            )
            return JsonResponse(response_data)

        except Exception as e:
            print(e)
            response_data['status'] = 'BAD'
            return JsonResponse(response_data)
