# alx_travel_app_0x00

### Database Modeling and Data Seeding

This app defines models for Listings, Bookings, and Reviews.  
It also includes a Django management command to populate the database with sample listings.

#### Run Seeder
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed

