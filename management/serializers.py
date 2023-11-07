# management/serializers.py

from rest_framework import serializers
from .models import AffiliateProduct

class AffiliateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateProduct
        fields = '__all__'
