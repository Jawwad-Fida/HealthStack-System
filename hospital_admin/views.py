from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from hospital.models import Hospital_Information, User
from doctor.models import Doctor_Information
from hospital.models import Patient
from .forms import AdminUserCreationForm, AddHospitalForm, EditHospitalForm,AddEmergencyForm, EditEmergencyForm
from .models import Admin_Information


# Create your views here.


def admin_home(request):
    return render(request, 'hospital_admin/index.html')


def logoutAdmin(request):
    logout(request)
    messages.info(request, 'User Logged out')
    return redirect('admin_login')


def admin_login(request):
    return render(request, 'hospital_admin/login.html')


def admin_login(request):
    # page = 'patient_login'
    if request.method == 'GET':
        return render(request, 'hospital_admin/login.html')
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


# def register(request):
#     return render(request, 'hospital_admin/register.html')


# def admin_register(request):
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     password1 = request.POST.get('password1')
#     if password == password1:
#         user = User(username=username, email=email, password=password)
#         user.save()
#         return redirect('admin_login')
#     else:
#         messages.error(request, 'Password does not match')
#         return render(request, 'hospital_admin/register.html')


def admin_register(request):
    page = 'hospital_admin/register'
    form = AdminUserCreationForm()

    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            # commit=False --> don't save to database yet (we have a chance to modify object)
            user = form.save(commit=False)
            user.is_hospital_admin = True
            user.save()

            messages.success(request, 'User account was created!')

            # After user is created, we can log them in
            #login(request, user)
            return redirect('admin_login')

        else:
            messages.error(
                request, 'An error has occurred during registration')
    # else:
    #     form = AdminUserCreationForm()

    context = {'page': page, 'form': form}
    return render(request, 'hospital_admin/register.html', context)


def admin_forgot_password(request):
    return render(request, 'hospital_admin/forgot-password.html')


def admin_profile(request):
    return render(request, 'hospital_admin/profile.html')


def doctor_list(request):
    doctors = Doctor_Information.objects.all()
    return render(request, 'hospital_admin/doctor-list.html', {'all': doctors})


def invoice(request):
    return render(request, 'hospital_admin/invoice.html')


def invoice_report(request):
    return render(request, 'hospital_admin/invoice-report.html')


def lock_screen(request):
    return render(request, 'hospital_admin/lock-screen.html')


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital_admin/patient-list.html', {'all': patients})


def specialitites(request):
    return render(request, 'hospital_admin/specialities.html')


def appointment_list(request):
    return render(request, 'hospital_admin/appointment-list.html')


def transactions_list(request):
    return render(request, 'hospital_admin/transactions-list.html')


def emergency_details(request):
    hospitals = Hospital_Information.objects.all()
    return render(request, 'hospital_admin/emergency.html', {'all': hospitals})


def hospital_list(request):
    hospitals = Hospital_Information.objects.all()
    return render(request, 'hospital_admin/hospital-list.html', {'hospitals': hospitals})


def appointment_list(request):
    return render(request, 'hospital_admin/appointment-list.html')



def hospital_profile(request):
    return render(request, 'hospital-profile.html')



def admin_profile(request, pk):
    admin = Admin_Information.objects.get(user_id=pk)
    context = {'admin': admin}

    return render(request, 'hospital_admin/admin-profile.html', context)


# def add_hospital(request):
#     return render(request, 'hospital_admin/add-hospital.html')


def add_hospital(request):
    page = 'hospital-list'
    form = AddHospitalForm()

    if request.method == 'POST':
        form = AddHospitalForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            hospital = form.save(commit=False)
            hospital.save()

            messages.success(request, 'Hospital was created!')

            return redirect('hospital-list')

        else:
            messages.error(
                request, 'An error has occurred during input')
    # else:
    #     form = AddHospitalForm()

    context = {'page': page, 'form': form}
    return render(request, 'hospital_admin/add-hospital.html', context)


# def edit_hospital(request, pk):
#     hospital = Hospital_Information.objects.get(hospital_id=pk)
#     return render(request, 'hospital_admin/edit-hospital.html')

def edit_hospital(request, pk):

    hospital = Hospital_Information.objects.get(hospital_id=pk)
    form = EditHospitalForm(instance=hospital)  

    if request.method == 'POST':
        form = EditHospitalForm(request.POST, request.FILES,
                           instance=hospital)  
        if form.is_valid():
            form.save()
            return redirect('hospital-list')
        else:
            form = EditHospitalForm()

    context = {'hospital': hospital, 'form': form}
    return render(request, 'hospital_admin/edit-hospital.html', context)

def edit_emergency_information(request, pk):

    hospital = Hospital_Information.objects.get(hospital_id=pk)
    form = EditEmergencyForm(instance=hospital)  

    if request.method == 'POST':
        form = EditEmergencyForm(request.POST, request.FILES,
                           instance=hospital)  
        if form.is_valid():
            form.save()
            return redirect('emergency')
        else:
            form = EditEmergencyForm()

    context = {'hospital': hospital, 'form': form}
    return render(request, 'hospital_admin/edit-emergency-information.html', context)


def delete_hospital(request, pk):
	hospital = Hospital_Information.objects.get(hospital_id=pk)
	hospital.delete()
	return redirect('hospital-list')