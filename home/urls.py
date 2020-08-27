from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(r'', views.home, name="home"),
    path(r'prices/', views.prices, name="prices"),
    path(r'login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path(r'register/', views.register, name="register"),
]