from django import forms
from .models import Vehicle
import datetime
from django.contrib.auth.models import User

class VehicleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['id', 'owner_name', 'phone_no', 'licence_no', 'make', 'model', 'year', 'license_plate']  # Add other fields as needed

    def clean_year(self):
        year = self.cleaned_data['year']
        current_year = datetime.date.today().year
        if year > current_year:
            raise forms.ValidationError("Year cannot be in the future.")
        return year

    def clean_license_plate(self):
        license_plate = self.cleaned_data['license_plate']
        # Add any license plate format validation here (if applicable)
        return license_plate
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)


    ROLE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('normal_user', 'Normal User'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'role')  # Add 'role' to the fields

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user