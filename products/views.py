from django.shortcuts import render

# Create your views here.
# product/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import AffiliateProduct
from .serializers import AffiliateProductSerializer

@api_view(['POST'])
def create_affiliate_product(request):
    serializer = AffiliateProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_affiliate_products(request):
    products = AffiliateProduct.objects.all()
    serializer = AffiliateProductSerializer(products, many=True)
    return Response(serializer.data)
