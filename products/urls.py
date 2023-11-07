# product/urls.py
from django.urls import path
from .views import create_affiliate_product, list_affiliate_products

urlpatterns = [
    path('create/', create_affiliate_product, name='create-affiliate-product'),
    path('list/', list_affiliate_products, name='list-affiliate-products'),
]