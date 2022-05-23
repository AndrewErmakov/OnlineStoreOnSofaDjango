import io

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle, Spacer, SimpleDocTemplate
from reportlab.platypus.para import Paragraph

from store_app.models import Order


class GeneratePdfDetailsOrder:
    def __init__(self, order: Order, num_order: str):
        self.order = order
        self.num_order = num_order

        """Создание файлового буфер для приема данных PDF"""
        self.buffer = io.BytesIO()

        """Сборка всех частей отчета"""
        self.report_elements = []

    def generate_pdf(self):
        self.register_fonts()
        styles = self.set_need_styles()
        mapping_info_order = {
            0: [f'Заказ №{self.num_order}', styles['our_heading']],
            1: [f'Эл.почта покупателя: {self.order.buyer_email}', styles['our_info']],
            2: [f'Получатель: {self.order.recipient}', styles['our_info']],
            3: [f'Способ оплаты: {self.order.payment_method}', styles['our_info']]
        }

        for i in range(4):
            self.add_paragraph(mapping_info_order[i][0], mapping_info_order[i][1])

        table = self.fill_and_generate_table(order=self.order, need_font='FreeSans')
        self.report_elements.append(table)

        """ Создание объект PDF, используя буфер в качестве своего «файла»."""
        pdf = SimpleDocTemplate(self.buffer, pagesize=A4, title=f'Заказ №{self.num_order}')
        """Сборка данных"""
        pdf.build(self.report_elements)
        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        self.buffer.seek(0)

        return self.buffer

    @staticmethod
    def register_fonts():
        """Регистрация необходимых шрифтов"""
        pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
        pdfmetrics.registerFont(TTFont('FreeSansBold', 'FreeSansBold.ttf'))

    @staticmethod
    def set_need_styles():
        """Установка необходимых стилей для оформления отчета"""
        need_styles = getSampleStyleSheet()
        need_styles.add(ParagraphStyle(name='our_heading', alignment=TA_CENTER, fontName='FreeSansBold', fontSize=16))
        need_styles.add(ParagraphStyle(name='our_info', alignment=TA_LEFT, fontName='FreeSans', fontSize=12))
        return need_styles

    @staticmethod
    def fill_and_generate_table(order: Order, need_font):
        """
            Генерация данных для таблицы: инфо о товарах в заказе
        """
        data_to_table = [
            ['Наименование товара', 'Цена товара', 'Количество', 'Сумма в рублях']
        ]

        for product_in_order in order.product_in_order.all():
            data_to_table.append(
                [
                    product_in_order.product.name,
                    product_in_order.product.price,
                    product_in_order.quantity,
                    product_in_order.quantity * product_in_order.product.price
                ]
            )
        data_to_table.append(['Итого', order.total_price])

        generated_table = Table(data_to_table)
        table_style = TableStyle(
            [
                ('FONTNAME', (0, 0), (-1, -1), need_font),
                ('BOX', (0, 0), (-1, -1), 2, colors.black),
                ('GRID', (0, 0), (-1, -2), 2, colors.black)
            ]
        )
        generated_table.setStyle(table_style)
        return generated_table

    def add_paragraph(self, info, style):
        self.report_elements.append(Paragraph(info, style))
        self.report_elements.append(Spacer(1, 10))
