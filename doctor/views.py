import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import DoctorUserCreationForm, DoctorForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from hospital.models import User, Patient
from .models import Doctor_Information, Appointment

import random
import string

# Create your views here.


def generate_random_string():
    N = 8
    string_var = ""
    string_var = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=N))
    return string_var


def doctor_change_password(request):
    return render(request, 'doctor-change-password.html')


def schedule_timings(request):
    return render(request, 'schedule-timings.html')


def patient_id(request):
    return render(request, 'patient-id.html')

def appointments(request):
    return render(request, 'appointments.html')


def logoutDoctor(request):
    logout(request)
    messages.info(request, 'User Logged out')
    return redirect('doctor-login')


def doctor_register(request):
    page = 'doctor-register'
    form = DoctorUserCreationForm()

    if request.method == 'POST':
        form = DoctorUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            # commit=False --> don't save to database yet (we have a chance to modify object)
            user = form.save(commit=False)
            user.is_doctor = True
            # user.username = user.username.lower()  # lowercase username
            user.save()

            messages.success(request, 'User account was created!')

            # After user is created, we can log them in
            #login(request, user)
            return redirect('doctor-login')

        else:
            messages.error(
                request, 'An error has occurred during registration')
    # else:
    #     form = DoctorUserCreationForm()

    context = {'page': page, 'form': form}
    return render(request, 'doctor-register.html', context)


def doctor_login(request):
    # page = 'patient_login'
    if request.method == 'GET':
        return render(request, 'doctor-login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('doctor-dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'doctor-login.html')


def doctor_dashboard(request):
    if request.user.is_doctor:
        # doctor = Doctor_Information.objects.get(user_id=pk)
        doctor = Doctor_Information.objects.get(user=request.user)
    else:
        redirect('doctor-logout')
    
    context = {'doctor': doctor}
    return render(request, 'doctor-dashboard.html', context)



def doctor_profile_settings(request):

    if request.user.is_doctor:
        doctor = Doctor_Information.objects.get(user=request.user)
    
        form = DoctorForm(instance=doctor)

        if request.method == 'POST':
            form = DoctorForm(request.POST, request.FILES,instance=doctor)
            if form.is_valid():
                form.save()
                return redirect('doctor-dashboard')
            else:
                form = DoctorForm()
    else:
        redirect('doctor-logout')

    context = {'doctor': doctor, 'form': form}
    return render(request, 'doctor-profile-settings.html', context)


def booking_success(request):
    return render(request, 'booking-success.html')


def booking(request, pk):
    patient = request.user.patient
    doctor = Doctor_Information.objects.get(doctor_id=pk)

    if request.method == 'POST':
        appointment = Appointment(patient=patient, doctor=doctor)
        date = request.POST['date']
        time = request.POST['time']
        appointment_type = request.POST['appointment_type']

        appointment.date = date
        appointment.time = time
        appointment.appointment_status = 'pending'
        appointment.serial_number = generate_random_string()
        appointment.appointment_type = appointment_type
        appointment.save()
        return redirect('patient-dashboard')

    context = {'patient': patient, 'doctor': doctor}
    return render(request, 'booking.html', context)


def doctor_profile(request, pk):
    # request.user --> get logged in user
    if request.user.is_patient:
        patient = request.user.patient
    else:
        patient = None
    
    doctor = Doctor_Information.objects.get(doctor_id=pk)
    context = {'doctor': doctor, 'patient': patient}
    
    return render(request, 'doctor-profile.html', context)


def my_patients(request):
    if request.user.is_doctor:
        doctor = Doctor_Information.objects.get(user=request.user)
        patients = Patient.objects.all()
    else:
        redirect('doctor-logout')
    
    
    context = {'doctor': doctor, 'patients': patients}
    return render(request, 'my-patients.html', context)


# def patient_profile(request):
#     return render(request, 'patient_profile.html')

def patient_profile(request):
    patient = Patient.objects.all()
    context = {'patient': patient}
    return render(request, 'patient_profile.html', context)

def view_report(request):
    return render(request, 'view-report.html')

def add_report(request):
    return render(request, 'add-report.html')


def prescription_view(request):
    return render(request, 'prescription-view.html')

def add_prescription(request):
    return render(request, 'add-prescription.html')

