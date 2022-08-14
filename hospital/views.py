import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, PatientForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver

from .models import Patient, User
from doctor.models import Doctor_Information, Appointment

from sslcommerz.models import Payment


# Create your views here.

# function to return views for the urls


def hospital_home(request):
    return render(request, 'index-2.html')


def change_password(request):
    return render(request, 'change-password.html')


def add_billing(request):
    return render(request, 'add-billing.html')


def appointments(request):
    return render(request, 'appointments.html')


def edit_billing(request):
    return render(request, 'edit-billing.html')


def edit_prescription(request):
    return render(request, 'edit-prescription.html')


def forgot_password_patient(request):
    return render(request, 'forgot-password-patient.html')


def privacy_policy(request):
    return render(request, 'privacy-policy.html')


def about_us(request):
    return render(request, 'about-us.html')


def forgot_password_doctor(request):
    return render(request, 'forgot-password-doctor.html')


def multiple_hospital(request):
    return render(request, 'multiple-hospital.html')


def chat(request):
    return render(request, 'chat.html')


def chat_doctor(request):
    return render(request, 'chat-doctor.html')


def hospital_profile(request):
    return render(request, 'hospital-profile.html')


# def login(request):
#     return render(request, 'login.html')

# def authenticate_user(email, password):
#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         return None
#     else:
#         if user.check_password(password):
#             return user


def login_user(request):
    page = 'patient_login'
    if request.method == 'GET':
        return render(request, 'patient-login.html')
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
            return redirect('patient-dashboard', pk=user.id)
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'patient-login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User Logged out')
    return redirect('login')


def patient_register(request):
    page = 'patient-register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            # commit=False --> don't save to database yet (we have a chance to modify object)
            user = form.save(commit=False)
            user.is_patient = True
            # user.username = user.username.lower()  # lowercase username
            user.save()

            messages.success(request, 'User account was created!')

            # After user is created, we can log them in
            #login(request, user)
            return redirect('login')

        else:
            messages.error(
                request, 'An error has occurred during registration')
    # else:
    #     form = CustomUserCreationForm()

    context = {'page': page, 'form': form}
    return render(request, 'patient-register.html', context)


def patient_profile(request, pk):
    patient = Patient.objects.get(patient_id=pk)
    context = {'patient': patient}

    return render(request, 'patient-profile.html', context)


def patient_dashboard(request, pk):
    patient = Patient.objects.get(user_id=pk)
    #appointments = Appointment.objects.all()
    appointments = Appointment.objects.filter(patient=patient)
    #payments = Payment.objects.filter(patient_id=patient.patient_id).filter(payment_type='appointment')
    
    # payments = Payment.objects.filter(patient=patient).filter(payment_type='appointment')
    payments = Payment.objects.filter(patient=patient).filter(appointment__in=appointments).filter(payment_type='appointment')

    context = {'patient': patient, 'appointments': appointments, 'payments': payments}

    return render(request, 'patient-dashboard.html', context)


def profile_settings(request, pk):

    # profile = request.user.profile
    patient = Patient.objects.get(user_id=pk)
    form = PatientForm(instance=patient)  # instance=patient

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES,
                           instance=patient)  # instance=patient
        if form.is_valid():
            form.save()
            return redirect('patient-dashboard', pk=pk)
        else:
            form = PatientForm()

    context = {'patient': patient, 'form': form}
    return render(request, 'profile-settings.html', context)


def search(request, pk):
    patient = Patient.objects.get(user_id=pk)

    doctors = Doctor_Information.objects.all()

    context = {'patient': patient, 'doctors': doctors}

    return render(request, 'search.html', context)


def payment(request):
    return render(request, 'checkout.html')
