from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.home, name="home"),
    path(r'prices/', views.prices, name="prices"),
    path(r'login/', views.login, name="login"),
]