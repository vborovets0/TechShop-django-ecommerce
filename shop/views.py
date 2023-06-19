from django.shortcuts import render
from django.views import generic

from shop.models import Product


class ProductListView(generic.ListView):
    model = Product
    context_object_name = "product_list"
    template_name = "shop/product.html"
    paginate_by = 5
