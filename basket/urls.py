from django.urls import path

from . import views

urlpatterns = [
    path("", views.basket_summary, name="basket_summery")
    ]

app_name = "basket"
