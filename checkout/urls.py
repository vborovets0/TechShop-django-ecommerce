from django.urls import path

from . import views
from .views import CancelView, CreateCheckoutSessionView, SuccessView

urlpatterns = [
    path("deliverychoices", views.deliverychoices, name="deliverychoices"),
    path("basket_update_delivery/", views.basket_update_delivery, name="basket_update_delivery"),
    path("delivery_address/", views.delivery_address, name="delivery_address"),
    path("payment_selection/", views.payment_selection, name="payment_selection"),

    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')

    # path("payment_complete/", views.payment_complete, name="payment_complete"),
    # path("payment_successful/", views.payment_successful, name="payment_successful"),
]

app_name = "checkout"
