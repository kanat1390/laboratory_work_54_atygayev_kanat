from django.urls import path
from .views import products_view

app_name = 'shop'

urlpatterns = [
    path('', products_view, name='products_view')
]
