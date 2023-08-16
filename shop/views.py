from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from shop.models import Product, Category


def category_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    context = {
        "category": category,
        "products": products
    }
    return render(request, "shop/category.html", context=context)


class HomePageView(TemplateView):
    template_name = "shop/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_list"] = Product.objects.all()[:4]
        return context


class ProductListView(generic.ListView):
    model = Product
    context_object_name = "products"
    template_name = "shop/all_products.html"


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

