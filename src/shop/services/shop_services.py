from ..models import Category, Product

def get_product_list():
    return Product.objects.all()