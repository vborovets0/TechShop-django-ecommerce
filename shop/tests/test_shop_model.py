import pytest

from django.urls import reverse

from shop.models import Product


def test_category_str(category):
    assert str(category) == category.name


def test_category_reverse(category):

    url = reverse("shop:category", kwargs={"pk": category.pk})

    assert category.get_absolute_url() == url


def test_product_str(product):
    assert str(product) == product.title


def test_product_reverse(product):
    url = reverse("shop:product-detail", kwargs={"pk": product.pk})

    assert product.get_absolute_url() == url


def test_product_manager_query(product, inactive_product):
    active_product = product

    # Query the active products using the manager
    active_products = Product.products.all()

    assert active_products.count() == 1
    assert active_product in active_products
    assert inactive_product not in active_products
