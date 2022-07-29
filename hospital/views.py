from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Doctor_Information

# Create your views here.

# function to return views for the urls


def hospital_home(request):
    return render(request, 'index-2.html')

def doctor_dashboard(request):
    return render(request, 'doctor-dashboard.html')

def doctor_profile(request):
    return render(request, 'doctor-profile.html')

def doctor_change_password(request):
    return render(request, 'doctor-change-password.html')

def change_password(request):
    return render(request, 'change-password.html')

def search(request):
    return render(request, 'search.html')    

def doctor_register(request):
    return render(request, 'doctor-register.html')

def doctor_profile_settings(request):
    return render(request, 'doctor-profile-settings.html')

def my_patients(request):
    return render(request, 'my-patients.html')


