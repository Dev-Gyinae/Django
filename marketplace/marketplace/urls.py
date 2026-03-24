from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.views import index, contact, services, products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('items/', include('item.urls')),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('products/', products, name='products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
