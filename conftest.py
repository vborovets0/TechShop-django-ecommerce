import pytest
from pytest_factoryboy import register
from django.urls import reverse

from basket.basket import Basket
from orders.models import Order
from tests.factories import (
    CategoryFactory,
    ProductFactory,
    UserBaseFactory,
    AddressFactory, BasketFactory
)

register(CategoryFactory)
register(ProductFactory)
register(UserBaseFactory)
register(AddressFactory)
register(BasketFactory)


@pytest.fixture
def category(db, category_factory):
    category = category_factory.create()
    return category


@pytest.fixture
def product(db, product_factory):
    product = product_factory.create()
    return product


@pytest.fixture
def inactive_product(db, product_factory):
    inactive_product = product_factory.create()
    inactive_product.is_active = False
    inactive_product.save()
    return inactive_product


@pytest.fixture
def product_with_category(db, product_factory, category):
    product = product_factory.create()
    product.category = category
    product.save()
    return product


@pytest.fixture
def multiproducts(db, product_factory):

    return [product_factory.create() for _ in range(10)]

@pytest.fixture
def userbase(db, user_base_factory):
    new_user = user_base_factory.create()
    return new_user


@pytest.fixture
def adminuser(db, user_base_factory):
    new_customer = user_base_factory.create(user_name="admin_user", is_staff=True, is_superuser=True)
    return new_customer


@pytest.fixture
def address(db, address_factory):
    new_address = address_factory.create()
    return new_address


@pytest.fixture
def basket_setup(db, client, userbase, multiproducts):
    client.post(reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
    client.post(reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)


@pytest.fixture
def test_order(userbase):
    return Order.objects.create(order_key="unique_order_key", user=userbase, total_paid=60)


