from django.shortcuts import render, redirect
from django.http import HttpResponse
from .services import shop_services
from .forms import CategoryForm, ProductForm
from django.urls import reverse
# Create your views here.

def products_view(request):
    category_name = request.GET.get('category')
    if category_name:
        product_list = shop_services.get_product_list_by_category_name(category_name)
    else:
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
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product = form.save()
        return redirect(reverse('shop:product', kwargs={'pk':product.id}))
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

def categories_view(request):
    category_list = shop_services.get_category_list()
    context = {
        'category_list': category_list,
    }
    return render(request, 'shop/category_list.html', context)

def category_edit_view(request, pk):
    category = shop_services.get_category_by_pk(pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('shop:categories')
    context={
        'form':form,
    }
    return render(request, 'shop/category_edit.html', context)


    

