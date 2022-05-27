from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store_app.urls')),
    path('accounts/', include('accounts_app.urls')),
    path('captcha/', include('captcha.urls')),
    path('management/', include('management_app.urls')),
]
