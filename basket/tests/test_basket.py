import pytest

from django.urls import reverse
from shop.models import Product


@pytest.fixture
def products(category):
    products = []
    for i in range(1, 4):
        product = Product.objects.create(
            category=category,
            title=f'test {i}',
            price='20.00'
        )
        products.append(product)
    return products

@pytest.fixture
def basket_setup(client, products):
    client.post(reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
    client.post(reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)


@pytest.mark.django_db
def test_basket_url(client):
    """
    Test homepage response status
    """
    response = client.get(reverse('basket:basket_summary'))
    assert response.status_code == 200


def test_basket_add(client, basket_setup):
    """
    Test adding items to the basket
    """
    response = client.post(reverse('basket:basket_add'), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True)
    assert response.json() == {'qty': 4}

    response = client.post(reverse('basket:basket_add'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
    assert response.json() == {'qty': 3}


def test_basket_update(client, basket_setup):
    """
    Test updating items from the basket
    """
    response = client.post(reverse('basket:basket_update'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
    assert response.json() == {'qty': 2, 'subtotal': '40.00'}


def test_basket_delete(client, basket_setup):
    """
    Test deleting items from the basket
    """
    response = client.post(reverse('basket:basket_delete'), {"productid": 2, "action": "post"}, xhr=True)
    assert response.json() == {'qty': 1, 'subtotal': '20.00'}