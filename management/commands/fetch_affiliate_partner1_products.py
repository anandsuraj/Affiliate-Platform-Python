# management/commands/fetch_affiliate_partner1_products.py
from django.core.management.base import BaseCommand
from management.utils import fetch_and_update_products

class Command(BaseCommand):
    help = 'Fetch products from affiliate partner 1'

    def handle(self, *args, **options):
        affiliate_partner = 'partner1'  # Replace with the actual affiliate partner identifier
        fetch_and_update_products(affiliate_partner)
