from django.contrib.auth.models import AbstractUser
from django.db import models

#class CustomUser(AbstractUser):
#    phone_no = models.CharField(max_length=20)
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    Group.objects.get_or_create(name='Super Admin')
    Group.objects.get_or_create(name='Admin')
    Group.objects.get_or_create(name='Editor')
    Group.objects.get_or_create(name='Normal User')

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=20)
    licence_no = models.CharField(max_length=50)
    # ... other fields ...

class Vehicle(models.Model):
    # Define fields for your vehicle information
    make = models.CharField(max_length=100, default='Prado')
    model = models.CharField(max_length=100, default='Toyota')
    year = models.IntegerField(default='2024')
    license_plate = models.CharField(max_length=20, default='ABC-K214')
    owner_name = models.CharField(max_length=255, default='Peter Gwadenya')  # Add owner_name field
    phone_no = models.CharField(max_length=20, default='254111791418')  # Add phone_no field
    licence_no = models.CharField(max_length=50, default='DRV-K204')  # Set default to an empty string

class VehicleLog(models.Model):
    user = models.CharField(max_length=100)  # Assuming username is stored
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} logged {self.vehicle.license_plate} at {self.latitude}, {self.longitude} on {self.timestamp}"