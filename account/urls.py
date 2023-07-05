from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.account_registration, name="register"),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
    # User dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

]

app_name = "account"
