from django.urls import path

from payment import views

urlpatterns = [
    path('', views.BasketView, name='basket'),
    # path('orderplaced/', views.order_placed, name='order_placed'),
    # path('error/', views.Error.as_view(), name='error'),
    # path('webhook/', views.stripe_webhook),
]

app_name = "payment"

