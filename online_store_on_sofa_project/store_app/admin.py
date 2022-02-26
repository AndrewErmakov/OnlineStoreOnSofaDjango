from django.contrib import admin
from store_app.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'sale_start_time', 'category', 'avg_rating')
    list_display_links = ('name', 'description')
    search_fields = ('name', 'description', 'price', 'category', 'avg_rating')
    date_hierarchy = 'sale_start_time'


@admin.register(ImageProduct)
class ImageProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    list_display_links = ['product']
    search_fields = ('product',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'text', 'author', 'rating', 'created_at')
    list_display_links = ['product', 'text']
    search_fields = ('product', 'text', 'author', 'rating',)


@admin.register(WarehouseProducts)
class WarehouseProductsAdmin(admin.ModelAdmin):
    list_display = ('product', 'count_products')
    list_display_links = ['product', 'count_products']
    search_fields = ('product', 'count_products',)


@admin.register(Cart)
class CartUserAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']
    search_fields = ('products', 'user',)


@admin.register(ProductInCart)
class CountProductInCartAdmin(admin.ModelAdmin):
    list_display = ('product', 'count_product_in_cart', 'cart_user')
    list_display_links = ['product']
    search_fields = ('product', 'count_product_in_cart',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['num_order', 'created_at', 'recipient', 'buyer_email', 'total_price', 'payment_method',
                    'method_receive_order', 'date_order']
    list_display_links = ['num_order', 'created_at', 'recipient', 'buyer_email', 'total_price', 'payment_method',
                          'method_receive_order', 'date_order']
    search_fields = ('num_order', 'created_at', 'recipient', 'buyer_email', 'total_price', 'payment_method',
                     'method_receive_order', 'date_order')


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ['name_recipient', 'surname_recipient', 'phone_recipient']
    list_display_links = ['name_recipient', 'surname_recipient', 'phone_recipient']
    search_fields = ('name_recipient', 'surname_recipient', 'phone_recipient',)


@admin.register(ProductsInOrder)
class CountProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'count_product_in_order', 'order']
    list_display_links = ['product', 'count_product_in_order']
    search_fields = ('product', 'count_product_in_order', 'order')


@admin.register(FeedBackWithClient)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name_client', 'phone_client', 'email_client', 'question_client', 'given_feedback']
    list_display_links = ['name_client', 'phone_client', 'email_client', 'question_client', 'given_feedback']
    search_fields = ('name_client', 'phone_client', 'email_client', 'question_client', 'given_feedback')


admin.site.register(Category)
