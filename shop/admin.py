from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Seller, Category, Product


@admin.register(Seller)
class DriverAdmin(UserAdmin):

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )


admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title", "seller", "price",
        "in_stock", "created", "updated",
    )
    search_fields = ("title", "seller",)
    list_filter = ("in_stock",)

