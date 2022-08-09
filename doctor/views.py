import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import DoctorUserCreationForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def doctor_dashboard(request):
    return render(request, 'doctor-dashboard.html')


def doctor_profile(request):
    return render(request, 'doctor-profile.html')


def doctor_change_password(request):
    return render(request, 'doctor-change-password.html')


def doctor_profile_settings(request):
    return render(request, 'doctor-profile-settings.html')


# def login_user(request):
#     page = 'patient_login'
#     if request.method == 'GET':
#         return render(request, 'patient-login.html')
#     elif request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, 'Username does not exist')

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('hospital_home')
#         else:
#             messages.error(request, 'Invalid username or password')

#     return render(request, 'patient-login.html')


# def logoutUser(request):
#     logout(request)
#     messages.info(request, 'User Logged out')
#     return redirect('login')

# def doctor_register(request):
#     page = 'doctor-register'
#     form = DoctorUserCreationForm()

#     if request.method == 'POST':
#         form = DoctorUserCreationForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             # commit=False --> don't save to database yet (we have a chance to modify object)
#             user = form.save(commit=False)
#             # user.username = user.username.lower()  # lowercase username
#             user.save()

#             messages.success(request, 'Doctor account was created!')

#             # After user is created, we can log them in
#             #login(request, user)
#             return redirect('login')

#         else:
#             messages.error(
#                 request, 'An error has occurred during registration')

#     context = {'page': page, 'form': form}
#     return render(request, 'doctor-register.html', context)


# def doctor_register(request):
#     return render(request, 'doctor-register.html')


def logoutUser(request):
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
            # user.username = user.username.lower()  # lowercase username
            user.save()

            messages.success(request, 'User account was created!')

            # After user is created, we can log them in
            #login(request, user)
            return redirect('doctor-login')

        else:
            messages.error(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'doctor-register.html', context)


def doctor_login(request):
    return render(request, 'doctor-login.html')


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
            return redirect('hospital_home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'doctor-login.html')
