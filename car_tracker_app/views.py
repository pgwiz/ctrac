from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle, UserProfile
from .forms import VehicleRegistrationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, UserForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy  # Import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme


def is_admin_or_superadmin(user):
    return user.is_authenticated and (user.groups.filter(name='Admin').exists() or user.groups.filter(name='Super Admin').exists())

@login_required  # Ensure the user is logged in
@user_passes_test(is_admin_or_superadmin)  # Check user's group
def manage_vehicles(request):
    vehicles = Vehicle.objects.filter(
        phone_no=request.user.userprofile.phone_no
    )
    return render(request, 'manage_vehicles.html', {'vehicles': vehicles})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)
    
class MyPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'  # Or your custom template
    success_url = reverse_lazy('manage_users')  # Redirect to manage_users on success


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

#def login(request):
#    return render(request, 'lr.html')

def docu(request):
    return render(request, 'documentation.html')

def t_location(request):
    return render(request, 'location.html')


def login_view(request):
    next_url = request.GET.get('next')  # Fetch the URL the user tried to access
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
         
    if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        return redirect(next_url)
    return redirect('index')  # Default page after login

    return render(request, 'login.html')
def manage_users_view(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})

def delete_user_view(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('manage_users')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Get the group based on the selected role
            role = form.cleaned_data.get('role')
            if role == 'super_admin':
                group = Group.objects.get(name='Super Admin')  # Assuming you have these groups created
            elif role == 'admin':
                group = Group.objects.get(name='Admin')
            elif role == 'editor':
                group = Group.objects.get(name='Editor')
            else:  # 'normal_user'
                group = Group.objects.get(name='Normal User')

            user.groups.add(group)  # Add the user to the selected group
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def edit_user_view(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})