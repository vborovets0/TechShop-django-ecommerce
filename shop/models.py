from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


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

    def get_absolute_url(self):
        return reverse("shop:category", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField(blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="product_seller")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    image = models.ImageField(upload_to="images/", default="images/default.png")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = "Products"
        ordering = ["-created"]

    def get_absolute_url(self):
        return reverse("shop:product-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
