from rest_framework import serializers
from .models import Location, Hospital

"""
LocationSerializer is used to serialize the Location model 
"""

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'address', 'latitude', 'longitude')

class HospitalSerializer(serializers.ModelSerializer):
    location = LocationSerializer() # Embed the location object in the hospital object

    class Meta:
        model = Hospital
        fields = ('id', 'name', 'beds_available', 'location')
