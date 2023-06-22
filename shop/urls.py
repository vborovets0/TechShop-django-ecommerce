from django.urls import path

from .views import ProductListView, ProductDetailView, category_list

urlpatterns = [
    path("", ProductListView.as_view(), name="index"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("category/<int:pk>", category_list, name="category"),
    ]

app_name = "shop"
