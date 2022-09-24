from django.urls import path
from .views import products_view, product_view, product_add_view

app_name = 'shop'

urlpatterns = [
    path('', products_view, name='products'),
    path('products/<int:pk>/',product_view, name='product'),
    path('products/add/', product_add_view, name='product_add'),
]
