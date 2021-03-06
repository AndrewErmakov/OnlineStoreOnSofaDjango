from django.urls import path

from .views import AddCommentView, AddProductToCartView, CartView, ContactsPageView, \
    CreatedOrderView, DeleteProductInCartView, FeedbackView, GenerateOrderPdfView, \
    HistoryOrdersView, IncreaseCountProductsView, OrderingPaymentDeliveryView, \
    OrderingPaymentOnlineView, ProductDetailsView, ProductListView, \
    ReduceCountProductsView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path(
        'product/<int:pk>/',
        ProductDetailsView.as_view(),
        name='product_details',
    ),

    # product page
    path('new_comment', AddCommentView.as_view(), name='add_new_comment'),
    path('add_product_to_basket', AddProductToCartView.as_view(), name='add_product_to_basket'),
    # cart page
    path('cart', CartView.as_view(), name='user_cart_page'),
    path(
        'delete_product_in_cart',
        DeleteProductInCartView.as_view(),
        name='delete_product_in_cart',
    ),
    path(
        'reduce_count_products',
        ReduceCountProductsView.as_view(),
        name='reduce_count_products',
    ),
    path(
        'increase_count_products',
        IncreaseCountProductsView.as_view(),
        name='increase_count_products',
    ),
    # ordering
    path(
        'ordering/payment_delivery',
        OrderingPaymentDeliveryView.as_view(),
        name='ordering_payment_delivery',
    ),
    path(
        'ordering/payment_online',
        OrderingPaymentOnlineView.as_view(),
        name='ordering_payment_online',
    ),
    path(
        'order_created/<int:encrypted_order_num>/<int:key>/',
        CreatedOrderView.as_view(),
        name='order_created',
    ),
    path(
        'history_orders',
        HistoryOrdersView.as_view(),
        name='history_orders',
    ),
    path(
        'pdf_details_order/<str:num_order>',
        GenerateOrderPdfView.as_view(),
        name='pdf_details_order',
    ),
    # footer
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('feedback_form', FeedbackView.as_view(), name='feedback_form'),

]
