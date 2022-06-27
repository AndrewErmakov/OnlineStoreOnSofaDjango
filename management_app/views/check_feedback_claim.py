from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views import View

from rolepermissions.mixins import HasPermissionsMixin

from store_app.models import ClientFeedback


class CheckFeedbackClaimView(HasPermissionsMixin, View):
    required_permission = 'feedback_with_clients'

    def get(self, request):
        try:
            feedback_requests = ClientFeedback.objects.filter(given_feedback=False).order_by('id')
            context = {
                'requests': feedback_requests,
                'username': request.user.username,
            }
            return render(
                request=request,
                template_name='check_requests_for_feedback.html',
                context=context,
            )
        except PermissionDenied:
            return redirect('home')
