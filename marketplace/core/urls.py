from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
]