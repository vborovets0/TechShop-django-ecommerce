from django.contrib import admin
from .models import Category, Product


admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title", "price",
        "in_stock", "created", "updated",
    )
    search_fields = ("title", "seller",)
    list_filter = ("in_stock",)

