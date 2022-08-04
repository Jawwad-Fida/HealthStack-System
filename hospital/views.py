import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
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

# def login(request):
#     return render(request, 'login.html')
def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user

    return None

def signin(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	elif request.method == 'POST':
		email = request.POST.get('email')
		password= request.POST.get('pass')
		user = authenticate_user(email, password)
		if user is None:
			return render(request, 'login.html', {'error': 'Invalid username or password'})
		else:
			auth_login(request, user)
			return redirect( 'hospital_home')
	