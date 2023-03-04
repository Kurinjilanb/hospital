from django.urls import path
from rest_framework import routers
from hospitalapp.views import LocationList, HospitalList

router = routers.DefaultRouter()
# Automatically generate URL patterns for LocationList and HospitalList views


urlpatterns = [
    path('locations/', LocationList.as_view(), name='location-list'),
    path('hospitals/', HospitalList.as_view(), name='hospital-list'),
]

urlpatterns += router.urls
