from django.contrib import admin
from .models import Driver, VehicleSharing, Passenger

# Register your models here.

admin.site.register(Driver)
admin.site.register(VehicleSharing)
admin.site.register(Passenger)
