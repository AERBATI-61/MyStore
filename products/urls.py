from django.contrib import admin
from django.urls import path
from .views import *
from user.views import *
urlpatterns = [
    path('', indexView, name="index"),


    path('product-list/', ProductList.as_view(), name="product_list"),
    path('product/<slug:slug>', ProductDetail.as_view(), name="product_detail"),
    path('product-list/<slug:slug>', product_view_with_category, name="category_view_with_category"),
    path('product_create/', ProductCreate.as_view(), name="product_create"),
    path('product_update/<slug:slug>', ProductUpdate.as_view(), name="product_update"),
    path('product_delete/<slug:slug>', ProductDelete.as_view(), name="product_delete"),


    path('category_list/', CategoryList.as_view(), name="category_list"),
    path('category_create/', CategoryCreate.as_view(), name="category_create"),
    path('category_update/<int:id>/', CategoryUpdate.as_view(), name="category_update"),
    path('category_delete/<int:id>/', CategoryDelete.as_view(), name="category_delete"),

    path('login', loginUser, name="login"),
    path('register', registerUser, name="register"),
    path('logout', logoutUser, name="logout"),
]