from django.contrib import admin
from .models import Driver, Vehicle, Request, VehicleSharing, Passenger

# Register your models here.

admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Request)
admin.site.register(VehicleSharing)
admin.site.register(Passenger)
