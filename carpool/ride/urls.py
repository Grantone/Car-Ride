from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^today/$', views.ride_of_day, name='rideToday')
]
