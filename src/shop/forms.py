from dataclasses import fields
from django.forms import ModelForm
from .models import Product, Category
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'desc', 'category', 'price', 'image']
        labels = {
            'name':'Название товара',
            'desc':'Описание товара',
            'category':'Категория',
            'price':'Цена',
            'image':'Изображение',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control name-input'}),
            'category':forms.Select(attrs={'class':'form-control category-input'}),
            'price':forms.TextInput(attrs={'class':'form-control price-input'}),
            'image':forms.FileInput(attrs={'class':'form-control image-input'}),
        }
    

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'desc']
        labels = {
            'name':'Название товара',
            'desc':'Описание товара',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control name-input'}),
        }

