from django.urls import path
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    path(r'', views.home, name="index"),
    path(r'prices/', views.prices, name="prices"),
    path(r'login/', views.login_request, name='login'),
    path(r'register', views.register, name="register"),
    path(r'logout', views.logout_request, name="logout"),
    path(r'profile/', views.user_profile, name="profile"),
    path(r'user_exist', views.user_exist, name='user_exist')
]