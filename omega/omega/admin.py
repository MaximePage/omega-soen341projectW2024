from django.contrib import admin
from .models import Member, Reservation, Vehicle, Location, Review

admin.site.register(Member)
admin.site.register(Vehicle)
admin.site.register(Reservation)
admin.site.register(Location)
admin.site.register(Review)