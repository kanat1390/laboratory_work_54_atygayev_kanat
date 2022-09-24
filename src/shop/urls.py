from django.urls import path
from .views import products_view, product_view

app_name = 'shop'

urlpatterns = [
    path('', products_view, name='products_view'),
    path('products/<int:pk>/',product_view, name='product_view'),
]
