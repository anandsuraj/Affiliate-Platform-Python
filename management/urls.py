# management/urls.py

from django.urls import path
from .views import AffiliateProductList

urlpatterns = [
    path('affiliate-products/', AffiliateProductList.as_view(), name='affiliate-product-list'),
    # Add more URL patterns as needed for different views
]