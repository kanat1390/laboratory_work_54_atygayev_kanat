from django.shortcuts import render
from django.http import HttpResponse
from .services import shop_services
# Create your views here.

def products_view(request):
    product_list = shop_services.get_product_list()
    context = {
        'product_list': product_list
    }
    return render(request, 'shop/product_list.html', context)

def product_view(request, pk):
    product = shop_services.get_product_by_pk(pk=pk)
    context = {
        'product':product,
    }
    return render(request, 'shop/product_detail.html', context)

