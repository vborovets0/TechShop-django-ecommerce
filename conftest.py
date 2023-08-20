import pytest
from mixer.backend.django import mixer
from pytest_factoryboy import register


from tests.factories import CategoryFactory, ProductFactory

register(CategoryFactory)
register(ProductFactory)

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

