from django.shortcuts import render, get_object_or_404
from django.views import generic

from shop.models import Product, Category


def categories(request):
    return {
        "categories": Category.objects.all()
    }

def category_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    context = {
        "category": category,
        "products": products
    }
    return render(request, "shop/category.html", context=context)


class ProductListView(generic.ListView):
    model = Product
    context_object_name = "product_list"
    template_name = "shop/product.html"
    paginate_by = 5


class ProductDetailView(generic.DetailView):
    model = Product
