from django.contrib.auth.models import AbstractUser
from django.db import models


class Seller(AbstractUser):
    class Meta:
        verbose_name = "seller"
        verbose_name_plural = "sellers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Category(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField(blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="product_seller")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    image = models.ImageField(upload_to="images/")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ["-created"]

    def __str__(self):
        return self.title
