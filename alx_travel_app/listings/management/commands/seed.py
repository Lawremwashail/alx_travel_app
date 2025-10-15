from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        # Clear old data first
        Listing.objects.all().delete()

        listings_data = [
            {
                "title": "Luxury Beach Villa",
                "description": "A beautiful villa with ocean views and private beach access.",
                "price_per_night": 250.00,
                "location": "Mombasa"
            },
            {
                "title": "Cozy Mountain Cabin",
                "description": "A peaceful cabin in the mountains, perfect for a weekend retreat.",
                "price_per_night": 120.00,
                "location": "Aberdare"
            },
            {
                "title": "Downtown City Apartment",
                "description": "Modern apartment located in the heart of the city with great amenities.",
                "price_per_night": 180.00,
                "location": "Nairobi"
            },
            {
                "title": "Desert Safari Tent",
                "description": "A luxurious tent experience under the stars of the desert sky.",
                "price_per_night": 90.00,
                "location": "Isiolo"
            },
        ]

        for data in listings_data:
            Listing.objects.create(
                title=data["title"],
                description=data["description"],
                price_per_night=data["price_per_night"],
                location=data["location"]
            )

        self.stdout.write(self.style.SUCCESS("✅ Database seeded successfully with sample listings!"))

