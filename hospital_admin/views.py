from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from hospital.models import Hospital_Information, User
from doctor.models import Doctor_Information,Report
from sslcommerz.models import Payment
from hospital.models import Patient
from .forms import AdminUserCreationForm, AddHospitalForm, EditHospitalForm, EditEmergencyForm,AdminForm
from .models import Admin_Information
import random
import string


# Create your views here.

def admin_dashboard(request):
    # admin = Admin_Information.objects.get(user_id=pk)
    if request.user.is_hospital_admin:
        user = Admin_Information.objects.get(user=request.user)
        context = {'admin': user}
    return render(request, 'hospital_admin/admin-dashboard.html', context)
    
    # return render(request, 'hospital_admin/admin-dashboard.html', context)

def logoutAdmin(request):
    logout(request)
    messages.info(request, 'User Logged out')
    return redirect('admin_login')
            

def admin_login(request):
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
            return redirect('admin-dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'hospital_admin/login.html')




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



def doctor_list(request):
    if request.user.is_hospital_admin:
        user = Admin_Information.objects.get(user=request.user)
    doctors = Doctor_Information.objects.all()
    return render(request, 'hospital_admin/doctor-list.html', {'all': doctors, 'admin': user})


def invoice(request):
    return render(request, 'hospital_admin/invoice.html')


def invoice_report(request):
    return render(request, 'hospital_admin/invoice-report.html')


def lock_screen(request):
    return render(request, 'hospital_admin/lock-screen.html')


def patient_list(request):
    if request.user.is_hospital_admin:
        user = Admin_Information.objects.get(user=request.user)
    patients = Patient.objects.all()
    return render(request, 'hospital_admin/patient-list.html', {'all': patients, 'admin': user})


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


def hospital_admin_profile(request, pk):

    # profile = request.user.profile
    # get user id of logged in user, and get all info from table
    admin = Admin_Information.objects.get(user_id=pk)
    form = AdminForm(instance=admin)

    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES,
                          instance=admin)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard', pk=pk)
        else:
            form = AdminForm()

    context = {'admin': admin, 'form': form}
    return render(request, 'hospital_admin/hospital-admin-profile.html', context)



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

def generate_random_invoice():
    N = 4
    string_var = ""
    string_var = ''.join(random.choices(string.digits, k=N))
    string_var = "#INV-" + string_var
    return string_var

def create_invoice(request, pk):
    patient = Patient.objects.get(patient_id=pk)

    if request.method == 'POST':
        invoice = Payment(patient=patient)
        
        consulation_fee = request.POST['consulation_fee']
        report_fee = request.POST['report_fee']
        #total_ammount = request.POST['currency_amount']
        invoice.currency_amount = int(consulation_fee) + int(report_fee)
        invoice.consulation_fee = consulation_fee
        invoice.report_fee = report_fee
        invoice.invoice_number = generate_random_invoice()
        invoice.name = patient
        invoice.status = 'Pending'
    
        invoice.save()
        return redirect('patient-list')

    context = {'patient': patient}
    return render(request, 'hospital_admin/create-invoice.html', context)


def create_report(request, pk):
    if request.user.is_hospital_admin:
        user = Admin_Information.objects.get(user=request.user)
    doctors =Doctor_Information.objects.get(doctor_id=pk)

    if request.method == 'POST':
        patient = Patient.objects.get(serial_number=request.POST['patient_serial_number'])
        report = Report(patient=patient, doctor=doctors)
        test_name = request.POST['test_name']
        description = request.POST['description']
        result = request.POST['result']
        delivery_date = request.POST['delivery_date']

        # Save to report table
        report.test_name = test_name
        report.description = description
        report.result = result
        report.delivery_date = delivery_date
        report.save()

        return redirect('doctor-list')

    context = {'doctors': doctors, 'admin': user}
    return render(request, 'hospital_admin/create-report.html',context)

def add_pharmacist(request):
    return render(request, 'hospital_admin/add-pharmacist.html')
