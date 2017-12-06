from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    work = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Driver(models.Model):
    driver = models.OneToOneField(User, on_delete=models.CASCADE)
    liscence_no = models.CharField(
        _('liscence_no'), max_length=30, blank=False)
    scanned = models.ImageField(_('picture of driver\'s liscence'), blank=True)
    confirmed = models.BooleanField(_('confirmed'), default=False)


@receiver(post_save, sender=Driver)
def create_driver_profile(sender, instance, created, **kwargs):
    if created:
        DriverProfile(driver=instance)
    sender = Driver
    save_driver_profile
    instance.driverprofile.save()


class Vehicle(models.Model):
    make = models.CharField(_('vehicle make'), max_length=160, blank=False)
    plate = models.CharField(_('liscenced plate number'),
                             max_length=15, blank=False)
    seats = models.IntegerField(_('no of seats'), blank=False)
    type = models.CharField(_('vehicle type'), max_length=30,
                            blank=False)


class Request(models.Model):
    pick = models.CharField(_('pick up point'), max_length=256, blank=False, )
    dest = models.CharField(_('destination'), max_length=256, blank=False)
    status = models.CharField(
        _('status'), max_length=256, blank=False, default='pending')
    ride = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return "request from " + self.user.get_full_name()


class VehicleSharing(models.Model):
    start = models.CharField(max_length=30)
    destination = models.CharField(max_length=60)
    cost = models.IntegerField(blank=False)
    start_time = models.TimeField(max_length=60, blank=False)
    no_pass = models.IntegerField(_('no of passengers'), blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    ended = models.BooleanField(_('sharing ended'), default=False)

    def __str__(self):
        return self.start + " to " + self.dest

    def get_user(self):
        return self.user

    def get_absolute_url(self):
        return self.pk


class Passenger(models.Model):
    user = models.ForeignKey(User, null=True)
    passenger = models.CharField(max_length=30)
    scanned = models.ImageField(_('picture of passenger'), blank=True)
    confirmed = models.BooleanField(_('confirmed'), default=False)

    def __str__(self):
        return self.passenger
