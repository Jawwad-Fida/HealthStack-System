from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Doctor_Information

# Create your views here.

# function to return views for the urls


def hospital_home(request):
    return render(request, 'index-2.html')

def doctor_dashboard(request):
    return render(request, 'doctor-dashboard.html')
