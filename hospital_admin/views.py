from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
# Create your views here.

def admin_home(request):
    return render(request, 'hospital_admin/index.html')

def admin_login(request):
    return render(request, 'hospital_admin/login.html')
def admin_register(request):
    return render(request, 'hospital_admin/register.html')
def admin_forgot_password(request):
    return render(request, 'hospital_admin/forgot-password.html')
def admin_profile(request):
    return render(request, 'hospital_admin/profile.html')
def doctor_list(request):
    return render(request, 'hospital_admin/doctor-list.html')