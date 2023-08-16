from django.urls import path

from .views import (
    ProductListView,
    ProductDetailView,
    category_list,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, HomePageView)

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("all_products", ProductListView.as_view(), name="all-products"),
    path("category/<int:pk>", category_list, name="category"),
    # CRUD
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("product/create/", ProductCreateView.as_view(), name="product-create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete")
    ]

app_name = "shop"
