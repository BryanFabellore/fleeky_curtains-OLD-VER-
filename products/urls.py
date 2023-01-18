from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_products, name='products'),
     path('checkout/',views.checkout, name='checkout'),
]
