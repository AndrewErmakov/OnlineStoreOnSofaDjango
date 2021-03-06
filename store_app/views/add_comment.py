from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from store_app.models import Comment, Product


class AddCommentView(LoginRequiredMixin, View):
    """
        Добавление комментария (мнения по товару, его оценка)
    """

    def post(self, request):
        response_data = {}
        try:
            rating = request.POST.get('rating')
            text_comment = request.POST.get('text_comment')

            Comment.objects.create(
                rating=int(rating),
                text=text_comment,
                author=request.user,
                product=Product.objects.get(pk=request.POST.get('product_id')),
            )

            response_data['status'] = 'OK'
            response_data['rating'] = rating
            response_data['text_comment'] = text_comment
            response_data['user'] = f'{request.user.first_name} {request.user.last_name}'
            return JsonResponse(response_data)

        except Exception as e:
            print(e)
            response_data['status'] = 'BAD'
            return JsonResponse(response_data)
