from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle, UserProfile
from .forms import VehicleRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vehicle_data = {
        'ID': vehicle.id,
        'Owner Name': vehicle.owner_name,
        'Phone Number': vehicle.phone_no,
        'License Number': vehicle.licence_no,
        'Make': vehicle.make,
        'Model': vehicle.model,
        'Year': vehicle.year,
        'License Plate': vehicle.license_plate
    }
    return JsonResponse(vehicle_data)


def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vehicle.delete()
    messages.success(request, f'Vehicle {vehicle.model} has been deleted successfully')
    return redirect('manage_vehicles')


def manage_vehicles(request):
    vehicles = Vehicle.objects.filter(
        phone_no=request.user.userprofile.phone_no  # Access phone_no through UserProfile
    )
    return render(request, 'manage_vehicles.html', {'vehicles': vehicles})

def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        form = VehicleRegistrationForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, f'Vehicle {vehicle.model} has been updated successfully')
            return redirect('manage_vehicles')
    else:
        form = VehicleRegistrationForm(instance=vehicle)
    return render(request, 'register_vehicle.html', {'form': form})
    

def register_vehicle(request):
    if request.method == 'POST':
        form = VehicleRegistrationForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)  # Don't save yet
            vehicle.owner_name = request.user.get_full_name() 
            
            # Get or create the UserProfile for the current user
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            
            vehicle.phone_no = user_profile.phone_no  # Access phone_no through UserProfile
            vehicle.licence_no = user_profile.licence_no  # Access licence_no through UserProfile
            
            vehicle.save()  # Now save the vehicle with the user information
            messages.success(request, f'Vehicle {vehicle.model} has been registered with the no plate {vehicle.license_plate}')
            return redirect('track')
    else:
        form = VehicleRegistrationForm()
    return render(request, 'register_vehicle.html', {'form': form})

def index(request):
    return render(request, 'index.html')


def track(request):
    vehicles = Vehicle.objects.all()  # Fetch all vehicles from the database
    return render(request, 'track.html', {'vehicles': vehicles})

def track_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    context = {
        'vehicle': vehicle,
        'vehicle_data': {
            'ID': vehicle.id,
            'Owner Name': vehicle.owner_name,
            'Phone Number': vehicle.phone_no,
            'License Number': vehicle.licence_no,
            'Make': vehicle.make,
            'Model': vehicle.model,
            'Year': vehicle.year,
            'License Plate': vehicle.license_plate
        }
    }
    # ... your logic for the track_vehicle page (e.g., fetching and displaying vehicle data)
    return render(request, 'track_vehicle.html', {'vehicle': vehicle})

def login(request):
    return render(request, 'lr.html')

def docu(request):
    return render(request, 'documentation.html')
