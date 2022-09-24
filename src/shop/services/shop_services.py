from ..models import Category, Product
from django.shortcuts import get_object_or_404

def get_product_list():
    return Product.objects.all()

def get_product_by_pk(pk):
    return get_object_or_404(Product, pk=pk)