from django.http import FileResponse
from django.shortcuts import redirect
from django.views import View

from store_app.accessory_modules import GeneratePdfDetailsOrder
from store_app.mixins import CheckOrderDetailMixin
from store_app.models import Order


class GenerateOrderPdfView(CheckOrderDetailMixin, View):
    def get(self, request, num_order):
        """
            Генерация информации о заказе
        """
        try:
            order = Order.objects.get(num_order=num_order)
            generation_pdf = GeneratePdfDetailsOrder(order, num_order)
            result_pdf = generation_pdf.generate_pdf()

            return FileResponse(result_pdf, as_attachment=False, filename=f'Заказ №{num_order}.pdf')

        except Order.DoesNotExist:
            return redirect('home')
