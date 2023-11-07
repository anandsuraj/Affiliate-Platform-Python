# management/models.py
from django.db import models

class AffiliateProduct(models.Model):
    affiliate_partner = models.ForeignKey(AffiliatePartner, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed for your products

    def __str__(self):
        return self.name
