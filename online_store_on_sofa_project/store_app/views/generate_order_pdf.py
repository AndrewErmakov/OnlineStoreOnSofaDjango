from django.http import FileResponse
from django.views import View

from store_app.accessory_modules import GeneratePdfDetailsOrder
from store_app.mixins import CheckOrderDetailMixin
from store_app.models import Order


class GenerateOrderPdfView(CheckOrderDetailMixin, View):

    def get(self, request, num_str):
        """
            Генерация информации о заказе
        """
        order = Order.objects.get(num_order=num_str)
        generation_pdf = GeneratePdfDetailsOrder(order, num_str)
        result_pdf = generation_pdf.generate_pdf()

        return FileResponse(result_pdf, as_attachment=False, filename=f'Заказ №{num_str}.pdf')
