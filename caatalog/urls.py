from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),
    path('swaggatam/', views.swaggatam, name='swaggatam'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]