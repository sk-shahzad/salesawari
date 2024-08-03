from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name="login"),
    path('register', views.register, name="register"),
    path('registerUser/<str:user_type>/', views.registerUser, name="registerUser"),
    path('registerUser/<str:user_type>/', views.registerUser, name="register_user")

]