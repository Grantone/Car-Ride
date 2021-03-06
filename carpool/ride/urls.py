from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='index'),
    # url(r'^accounts/login/$', views.login, name='login'),
    # url(r'^accounts/logout/$', views.logout, {"next_page": '/'}),
    url('^today/$', views.ride_of_day, name='rideToday'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),
    url(r'^ride/(\d+)$', views.profile, name='profile'),
    url(r'^passenger/$', views.passenger, name='passenger'),
    url(r'^driver/(\d+)', views.index, name='driver'),
    url(r'^passenger_profile/(\d+)$',
        views.passenger_profile, name='passenger_profile'),
    url(r'^driver_profile/(\d+)$',
        views.driver_profile, name='driver_profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
