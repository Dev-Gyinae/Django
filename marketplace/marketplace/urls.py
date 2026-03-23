
from django.contrib import admin
from django.urls import path

from core.views import index, contact, services, products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('products/', products, name='products'),
]
