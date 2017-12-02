from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    work = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class DriverInfo(models.Model):
    driver = models.OneToOneField(User, on_delete=models.CASCADE)
    liscence_no = models.CharField(
        _('liscence_no'), max_length=30, blank=False)
    scanned = models.ImageField(_('picture of driver\'s liscence'), blank=True)
    confirmed = models.BooleanField(_('confirmed'), default=False)


class Vehicle(models.Model):
    make = models.CharField(_('vehicle make'), max_length=160, blank=False)
    plate = models.CharField(_('liscenced plate number'),
                             max_length=15, blank=False)
    seats = models.IntegerField(_('no of seats'), blank=False)
    type = models.CharField(_('vehicle type'), max_length=30,
                            blank=False)
