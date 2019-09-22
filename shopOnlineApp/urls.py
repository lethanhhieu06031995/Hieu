from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shoponline'
urlpatterns = [
    path('', views.index, name='index'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
]
