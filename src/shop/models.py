from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(null=False, blank=True, max_length=50)
    desc = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    desc = RichTextField(null=True, blank=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, blank=False, null=False, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    image = models.ImageField(null=True, blank=True, upload_to='products/images/')

    @property
    def get_price(self):
        return f'{self.price}$'

    def __str__(self):
        return self.name

