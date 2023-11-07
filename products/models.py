from django.db import models

# Create your models here.
# product/models.py
from django.db import models

class AffiliateProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    affiliate_link = models.URLField()

    def __str__(self):
        return self.name
