import pytest
from django.urls import reverse

from orders.models import Order, OrderItem
from orders.views import payment_confirmation


@pytest.mark.django_db
def test_add_to_order(client, userbase, basket_setup):

    # Log in the user
    client.force_login(userbase)

    response = client.post(
        reverse('orders:add'),
        {"action": "post", "order_key": "order123"},)

    assert response.status_code == 200
    assert Order.objects.filter(order_key="order123").exists()

    order = Order.objects.get(order_key="order123")
    prod = OrderItem.objects.filter(order=order)
    assert prod.count() == 2

    expected_response = {'success': 'Return something'}
    assert response.json() == expected_response


@pytest.mark.django_db
def test_payment_confirmation(userbase, test_order):
    order = test_order
    # Confirm payment for the order
    payment_confirmation(data="unique_order_key")

    # Check if the billing_status for the order is updated
    order.refresh_from_db()
    assert order.billing_status is True


@pytest.mark.django_db
def test_user_orders(client, userbase):
    # Log in the user
    client.force_login(userbase)

    # Create test orders for the user
    order1 = Order.objects.create(user=userbase, order_key="order_key_1",  total_paid=60, billing_status=True)
    order2 = Order.objects.create(user=userbase, order_key="order_key_2",  total_paid=60, billing_status=True)
    order3 = Order.objects.create(user=userbase, order_key="order_key_3",  total_paid=60, billing_status=False)

    # Make a GET request to the 'user_orders' view
    response = client.get(reverse('account:user_orders'))

    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if the response contains the expected orders
    orders_in_response = response.context['orders']
    assert order1 in orders_in_response
    assert order2 in orders_in_response
    assert order3 not in orders_in_response