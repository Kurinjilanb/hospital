from django.shortcuts import render, redirect, get_object_or_404
import requests
from .forms import HospitalForm
from .forms import LocationForm
from .models import Hospital
from .models import Location
import json
import hospital.settings as settings
from .models import Location, Hospital



def hospital_create(request):
    """
    hospital_create view function renders the hospital_form.html template # Docstring
    """
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm()
    return render(request, 'hospital/hospital_form.html', {'form': form})


def hospital_list(request):
    """
    hospital_list view function renders the hospital_list.html template # Docstring
    """
    hospitals = Hospital.objects.all()
    return render(request, 'hospital/hospital_list.html', {'hospitals': hospitals})


def hospital_update(request, hospital_id):
    hospital = Hospital.objects.get(id=hospital_id)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'hospital/hospital_form.html', {'form': form})


def driver_page(request):
    """
    driver_page view function renders the driver_page.html template # Docstring 
    """
    hospitals = Hospital.objects.all()
    context = {'hospitals': hospitals}
    return render(request, 'hospital/driver_page.html', context)


def update_hospital(request, pk):
    """
    update_hospital view function renders the update_hospital.html template # Docstring
    """
    # hospital = Hospital.objects.get(id=hospital_id)
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('driver_page')
    else:
        form = HospitalForm(instance=hospital)
    context = {'form': form}
    return render(request, 'hospital/update_hospital.html', context)


def delete_hospital(request, pk):
    """
    delete_hospital view function renders the delete_hospital.html template # Docstring
    """
    hospital = get_object_or_404(Hospital, pk=pk)
    hospital.delete()
    return redirect('driver_page')


def home(request):
    return render(request, 'home.html')


def navigate_to_destination(request):
    """
    navigate_to_destination view function renders the navigate_to_destination.html template # Docstring
    """
    url = 'https://www.googleapis.com/geolocation/v1/geolocate'
    params = {'key': settings.GOOGLE_MAP}

    # Send a POST request to the Geolocation API endpoint
    response = requests.post(url, params=params)

    # Parse the JSON response and extract the latitude and longitude coordinates
    result = json.loads(response.text)
    lat = result['location']['lat']
    lng = result['location']['lng']

    # Step 2: Use the Google Maps Directions API to generate turn-by-turn directions

    # Set up the Directions API endpoint and parameters
    url = 'https://maps.googleapis.com/maps/api/directions/json'
    params = {
        'origin': f'{lat},{lng}',
        'destination': 'Bangalore, India',
        'mode': 'driving',
        'key': settings.GOOGLE_MAP
    }

    # Send a GET request to the Directions API endpoint
    response = requests.get(url, params=params)

    # Parse the JSON response and extract the turn-by-turn directions
    result = json.loads(response.text)
    steps = result['routes'][0]['legs'][0]['steps']

    # Step 3: Use a navigation app on the user's mobile device to display the directions

    # Construct the navigation app URL and redirect the user to it
    url = f'https://www.google.com/maps/dir/?api=1&origin={lat},{lng}&destination=Bangalore, India&travelmode=driving'
    return redirect(url)


def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm()
    return render(request, 'location/add_location.html', {'form': form})


def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location/location_list.html', {'locations': locations})