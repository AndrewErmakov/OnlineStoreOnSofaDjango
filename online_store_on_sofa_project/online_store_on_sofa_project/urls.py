from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store_app.urls')),
    path('accounts/', include('accounts_app.urls')),
    path('captcha/', include('captcha.urls')),
    path('management/', include('management_app.urls')),
]
handler403 = 'store_app.views.error_403'
handler404 = 'store_app.views.error_404'
