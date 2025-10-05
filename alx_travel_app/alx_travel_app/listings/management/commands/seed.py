from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_data = [
            {"title": "Cozy Apartment", "description": "Nice city apartment", "price_per_night": 50.00, "location": "Nairobi"},
            {"title": "Beach House", "description": "House by the beach", "price_per_night": 120.00, "location": "Mombasa"},
            {"title": "Mountain Cabin", "description": "Quiet cabin in the mountains", "price_per_night": 80.00, "location": "Mt. Kenya"},
        ]

        for data in sample_data:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))

