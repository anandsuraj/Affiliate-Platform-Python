# management/views.py
from rest_framework import generics
from .models import AffiliateProduct
from .serializers import AffiliateProductSerializer

class AffiliateProductList(generics.ListCreateAPIView):
    queryset = AffiliateProduct.objects.all()
    serializer_class = AffiliateProductSerializer

# Define views for different affiliate partners if needed
