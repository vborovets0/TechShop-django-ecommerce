from django.shortcuts import render
from django.views import generic

from shop.models import Product, Category


def categories(request):
    return {
        "categories": Category.objects.all()
    }

class ProductListView(generic.ListView):
    model = Product
    context_object_name = "product_list"
    template_name = "shop/product.html"
    paginate_by = 5


class ProductDetailView(generic.DetailView):
    model = Product
