from django.contrib import admin
from .models import Profile, Driver, Vehicle, Request, VehicleSharing, PassengerInfo

# Register your models here.
admin.site.register(Profile)
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Request)
admin.site.register(VehicleSharing)
admin.site.register(Passenger)
