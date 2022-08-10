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
def invoice(request):
    return render(request, 'hospital_admin/invoice.html')
def invoice_report(request):
    return render(request, 'hospital_admin/invoice-report.html')
def lock_screen(request):
    return render(request, 'hospital_admin/lock-screen.html')
def patient_list(request):
    return render(request, 'hospital_admin/patient-list.html')
def hospital_list(request): 
    return render(request, 'hospital_admin/hospital-list.html')
def appointment_list(request):
    return render(request, 'hospital_admin/appointment-list.html')
def transactions_list(request):
    return render(request, 'hospital_admin/transactions-list.html')
def add_hospital(request): 
    return render(request, 'hospital_admin/add-hospital.html')
def edit_hospital(request):
    return render(request, 'hospital_admin/edit-hospital.html')
