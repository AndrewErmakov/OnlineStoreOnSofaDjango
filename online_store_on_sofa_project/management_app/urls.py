from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import AddProductImageView, AddProductView, AddReceivedProductToWarehouse, \
    ChangeCharacteristicsProductView, ChangeProductInfoView, CheckFeedbackClaimView, \
    GetSalesAnalyticsView, SendAnswerToClientFeedbackClaim

urlpatterns = [
    path(
        'feedback_with_clients/',
        CheckFeedbackClaimView.as_view(),
        name='feedback_with_clients',
    ),
    path(
        'response_to_request_feedback/',
        SendAnswerToClientFeedbackClaim.as_view(),
        name='response_to_request_feedback',
    ),

    path(
        'add_new_products/',
        AddProductView.as_view(),
        name='add_new_products',
    ),
    path(
        'add_images_for_product/',
        AddProductImageView.as_view(),
        name='add_images_for_product',
    ),
    path(
        'change_info_product/',
        ChangeProductInfoView.as_view(),
        name='change_info_product',
    ),

    path(
        'add_count_received_product_to_warehouse/product/<int:pk>/',
        AddReceivedProductToWarehouse.as_view(),
        name='add_count_received_product_to_warehouse',
    ),

    path(
        'change_characteristics_product/product/<int:pk>/',
        ChangeCharacteristicsProductView.as_view(),
        name='change_characteristics_product',
    ),

    path('get_analytics/sales/', GetSalesAnalyticsView.as_view(), name='get_sales_analytics'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
