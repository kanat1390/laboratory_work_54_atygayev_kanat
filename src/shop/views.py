from django.shortcuts import render, redirect
from django.http import HttpResponse
from .services import shop_services
from .forms import CategoryForm, ProductForm
from django.urls import reverse
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

def product_add_view(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        product = form.save()
        return redirect(reverse('shop:product', kwargs={'pk':product.id}))
    form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'shop/product_create.html', context)

def category_add_view(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        category = form.save()
        return redirect('shop:products')
    context = {
        'form': form,
    }
    return render(request, 'shop/category_create.html', context)

    

