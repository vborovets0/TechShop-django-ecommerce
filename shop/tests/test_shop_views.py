import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_category_list_view(client, category, product, product_with_category):

    url = reverse('shop:category', kwargs={'pk': category.pk})
    response = client.get(url)

    assert response.status_code == 200
    assert category == response.context['category']
    assert product_with_category in response.context['products']
    assert product not in response.context['products']


@pytest.mark.django_db
def test_home_page_view(client, multiproducts):
    response = client.get(reverse('shop:index'))
    assert response.status_code == 200
    product_list = response.context['product_list']
    assert len(product_list) == 4
