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


def doctor_profile(request):
    return render(request, 'doctor-profile.html')


def doctor_change_password(request):
    return render(request, 'doctor-change-password.html')


def my_patients(request):
    return render(request, 'my-patients.html')


def schedule_timings(request):
    return render(request, 'schedule-timings.html')


def patient_id(request):
    return render(request, 'patient-id.html')


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
            return redirect('doctor-dashboard', pk=user.id)
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'doctor-login.html')


# def doctor_dashboard(request):
#     return render(request, 'doctor-dashboard.html')

def doctor_dashboard(request, pk):
    doctor = Doctor_Information.objects.get(user_id=pk)
    context = {'doctor': doctor}

    return render(request, 'doctor-dashboard.html', context)


# def doctor_profile_settings(request):
#     return render(request, 'doctor-profile-settings.html')

# def doctor_profile_settings(request, pk):
#     doctor = Doctor_Information.objects.get(user_id=pk)
#     context = {'doctor': doctor}

#     return render(request, 'doctor-profile-settings.html', context)


def doctor_profile_settings(request, pk):

    # profile = request.user.profile
    # get user id of logged in user, and get all info from table
    doctor = Doctor_Information.objects.get(user_id=pk)
    form = DoctorForm(instance=doctor)

    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES,
                          instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor-dashboard', pk=pk)
        else:
            form = DoctorForm()

    context = {'doctor': doctor, 'form': form}
    return render(request, 'doctor-profile-settings.html', context)


def booking_success(request):
    return render(request, 'booking-success.html')


# def booking(request):
#     return render(request, 'booking.html')


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
        return redirect('patient-dashboard', pk=patient.user_id)

    context = {'patient': patient, 'doctor': doctor}
    return render(request, 'booking.html', context)
