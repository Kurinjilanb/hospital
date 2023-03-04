from django import forms
from .models import Hospital
from .models import Location

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'beds_available']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address', 'latitude', 'longitude']

