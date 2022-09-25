from django.urls import path
from .views import (
    products_view, 
    product_view, 
    product_add_view, 
    category_add_view,
    categories_view,
    category_edit_view,
    category_delete_view,
    product_edit_view,
    product_delete_view
    )

app_name = 'shop'

urlpatterns = [
    path('', products_view, name='products'),
    path('products/<int:pk>/',product_view, name='product'),
    path('products/add/', product_add_view, name='product_add'),
    path('categories/add/', category_add_view, name='category_add'),
    path('categories/', categories_view, name='categories'),
    path('categories/<int:pk>/edit/', category_edit_view, name='category_edit'),
    path('categories/<int:pk>/delete/', category_delete_view, name='category_delete'),
    path('products/<int:pk>/edit/', product_edit_view, name='product_edit'),
    path('products/<int:pk>/delete/', product_delete_view, name='product_delete')
]
