from ..models import Category, Product
from django.shortcuts import get_object_or_404

def get_product_list():
    return Product.objects.all()

def get_product_by_pk(pk):
    return get_object_or_404(Product, pk=pk)

def get_product_list_by_category_name(category_name):
    return Product.objects.filter(category__name=category_name)

def get_category_list():
    return Category.objects.all()

def get_category_by_pk(pk):
    return get_object_or_404(Category, pk=pk)
