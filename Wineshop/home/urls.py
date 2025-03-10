"""Wineshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import HomeView,view_category,View_product,register_1,view_address,cart,update_address_1,view_cart

urlpatterns = [

    path('home',HomeView,name='homePage'),
    path('view_category',view_category),
    path('View_product/<int:id>/', View_product),
    path('view_category',view_category),
    path('register_1',register_1),
    path('login/',auth_views.LoginView.as_view(template_name="login.html")),
    path('logout/',auth_views.LogoutView.as_view(template_name="logout.html")),
    path('view_address',view_address),
    path('View_product/<int:id>/cart', cart),
    path('update_address2',update_address_1),
    path('view_cart',view_cart)


]
