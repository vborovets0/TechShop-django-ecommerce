from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from shop.models import Product, Category


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
    paginate_by = 4


class ProductDetailView(generic.DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("shop:index")
    template_name = "shop/product_form.html"


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("shop:index")
    template_name = "shop/product_form.html"


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy("shop:index")

