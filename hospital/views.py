from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
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

def login(request):
    return render(request, 'login.html')

def add_billing(request):
	return render(request, 'add-billing.html')

def add_prescription(request):
	return render(request, 'add-prescription.html')

def appointments(request):
	return render(request, 'appointments.html')

def booking_success(request):
	return render(request, 'booking-success.html')

def booking(request):
	return render(request, 'booking.html')

def edit_billing(request):
	return render(request, 'edit-billing.html')

def edit_prescription(request):
	return render(request, 'edit-prescription.html')

def forgot_password(request):
	return render(request, 'forgot-password.html')

def patient_dashboard(request):
	return render(request, 'patient-dashboard.html')

def patient_profile(request):
	return render(request, 'patient-profile.html')

def privacy_policy(request):
	return render(request, 'privacy-policy.html')

def profile_settings(request):
	return render(request, 'profile-settings.html')

def register(request):
	return render(request, 'register.html')

def schedule_timings(request):
	return render(request, 'schedule-timings.html')

def signin(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	elif request.method == 'POST':
		e = request.POST.get('user')
		p = request.POST.get('pass')
		user = authenticate(username=e, password=p)
		if user is None:
			return render(request, 'login.html', {'error': 'Invalid username or password'})
		else:
			login(request, user)
			return render(request , 'index-2.html')