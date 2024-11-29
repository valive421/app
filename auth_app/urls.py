# auth_app/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Map root URL
    path('accounts/', include('accounts.urls')),
]
