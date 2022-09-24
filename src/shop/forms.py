from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'desc', 'category', 'price', 'image']



# class Product(models.Model):
#     name = models.CharField(null=False, blank=False, max_length=50)
#     desc = RichTextField(null=False, blank=False)
#     category = models.ForeignKey(to='Category', on_delete=models.CASCADE, blank=False, null=False, related_name='products')
#     created_at = models.DateTimeField(auto_now_add=True)
#     price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
#     image = models.ImageField(null=True, blank=True, upload_to='products/images/')