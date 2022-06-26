from django.http import JsonResponse
from django.views import View

from store_app.models import ClientFeedback


class FeedbackView(View):
    """Класс обработки отправки данных на заявку по получению обратной связи"""

    def post(self, request):
        response_data = {}
        try:
            ClientFeedback.objects.create(
                name=request.POST.get('name'),
                phone=request.POST.get('phone'),
                email=request.POST.get('email'),
                question=request.POST.get('question'),
            )
            response_data['status'] = 'OK'

        except Exception as e:
            print(e)
            response_data['status'] = 'BAD'

        return JsonResponse(response_data)
