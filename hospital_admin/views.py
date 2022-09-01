import email
from email.mime import image
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from hospital.models import Hospital_Information, User, Patient
from doctor.models import Doctor_Information,Report,Appointment
from sslcommerz.models import Payment
from .forms import AdminUserCreationForm, AddHospitalForm, EditHospitalForm, EditEmergencyForm,AdminForm
from .models import Admin_Information,specialization,service,hospital_department
import random,re
import string
from django.db.models import  Count


# Create your views here.
@login_required(login_url='admin-login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_dashboard(request):
    # admin = Admin_Information.objects.get(user_id=pk)
    if request.user.is_hospital_admin:
        user = Admin_Information.objects.get(user=request.user)
        total_patient_count = Patient.objects.annotate(count=Count('patient_id'))
        total_doctor_count = Doctor_Information.objects.annotate(count=Count('doctor_id'))
        pending_appointment = Appointment.objects.filter(appointment_status='pending').count()
        context = {'admin': user,'total_patient_count': total_patient_count,'total_doctor_count':total_doctor_count,'pending_appointment':pending_appointment, }
        return render(request, 'hospital_admin/admin-dashboard.html', context)
    
    # return render(request, 'hospital_admin/admin-dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutAdmin(request):
    logout(request)
    messages.info(request, 'User Logged out')
    return redirect('admin_login')
            

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

@login_required(login_url='admin-login')
def admin_forgot_password(request):
    return render(request, 'hospital_admin/forgot-password.html')


@login_required(login_url='admin-login')
def doctor_list(request):
    if request.user.is_hospital_admin:
        user = Admin_Information.objects.get(user=request.user)
    doctors = Doctor_Information.objects.all()
    return render(request, 'hospital_admin/doctor-list.html', {'all': doctors, 'admin': user})

@login_required(login_url='admin-login')
def invoice(request):
    return render(request, 'hospital_admin/invoice.html')

@login_required(login_url='admin-login')
def invoice_report(request):
    return render(request, 'hospital_admin/invoice-report.html')

@login_required(login_url='admin-login')
def lock_screen(request):
    return render(request, 'hospital_admin/lock-screen.html')

@login_required(login_url='admin-login')
def patient_list(request):
    if request.user.is_hospital_admin:
        user = Admin_Information.objects.get(user=request.user)
    patients = Patient.objects.all()
    return render(request, 'hospital_admin/patient-list.html', {'all': patients, 'admin': user})

@login_required(login_url='admin-login')
def specialitites(request):
    return render(request, 'hospital_admin/specialities.html')

@login_required(login_url='admin-login')
def appointment_list(request):
    return render(request, 'hospital_admin/appointment-list.html')

@login_required(login_url='admin-login')
def transactions_list(request):
    return render(request, 'hospital_admin/transactions-list.html')

@login_required(login_url='admin-login')
def emergency_details(request):
    hospitals = Hospital_Information.objects.all()
    return render(request, 'hospital_admin/emergency.html', {'all': hospitals})

@login_required(login_url='admin-login')
def hospital_list(request):
    hospitals = Hospital_Information.objects.all()
    return render(request, 'hospital_admin/hospital-list.html', {'hospitals': hospitals})

@login_required(login_url='admin-login')
def appointment_list(request):
    return render(request, 'hospital_admin/appointment-list.html')


@login_required(login_url='admin-login')
def hospital_profile(request):
    return render(request, 'hospital-profile.html')

@login_required(login_url='admin-login')
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


@login_required(login_url='admin-login')
def add_hospital(request):
    if  request.user.is_hospital_admin:
        user = Admin_Information.objects.get(user=request.user)

    if request.method == 'POST':
        hospital = Hospital_Information()
        specializations = specialization(hospital=hospital)
        services = service(hospital=hospital)
        departments = hospital_department(hospital=hospital)
        
        
        featured_image = request.FILES['featured_image']
        
        
        hospital_name = request.POST.get('hospital_name')
        address = request.POST.get('address')
        description = request.POST.get('description')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number') 
        hospital_type = request.POST.get('type')
        specialization_name = request.POST.getlist('specialization')
        department_name = request.POST.getlist('department')
        service_name = request.POST.getlist('service')


        hospital.name = hospital_name
        hospital.description = description
        hospital.address = address
        hospital.email = email
        hospital.phone_number =phone_number
        hospital.featured_image=featured_image 
        hospital.hospital_type=hospital_type
        
        specializations.specialization_name=specialization_name
        services.service_name = service_name
        departments.hospital_department_name = department_name 

        hospital.save()
        specializations.save()
        services.save()
        departments.save()

        return redirect('hospital-list')

    context = { 'admin': user}
    return render(request, 'hospital_admin/add-hospital.html',context)



# def edit_hospital(request, pk):
#     hospital = Hospital_Information.objects.get(hospital_id=pk)
#     return render(request, 'hospital_admin/edit-hospital.html')
@login_required(login_url='admin-login')
def edit_hospital(request, pk):
         if  request.user.is_hospital_admin:
             user = Admin_Information.objects.get(user=request.user)

             hospital = Hospital_Information.objects.get(hospital_id=pk)

             old_featured_image = hospital.featured_image

             if request.method == 'GET':
                    
                    specializations =specialization.objects.filter(hospital=hospital)
                    services=service.objects.filter(hospital=hospital)
                    departments =hospital_department.objects.filter(hospital=hospital)

                    context = {'hospital': hospital, 'specializations': specializations, 'services': services,'departments':departments} 
                    return render(request, 'hospital_admin/edit-hospital.html',context)

             elif request.method == 'POST':
                if 'featured_image' in request.FILES:
                    featured_image = request.FILES['featured_image']
                else:
                    featured_image = old_featured_image

                                
                    hospital_name = request.POST.get('hospital_name')
                    address = request.POST.get('address')
                    description = request.POST.get('description')
                    email = request.POST.get('email')
                    phone_number = request.POST.get('phone_number') 
                    hospital_type = request.POST.get('type')
                    specialization_name = request.POST.getlist('specialization')
                    department_name = request.POST.getlist('department')
                    service_name = request.POST.getlist('service')

                    hospital.name = hospital_name
                    hospital.description = description
                    hospital.address = address
                    hospital.email = email
                    hospital.phone_number =phone_number
                    hospital.featured_image =featured_image 
                    hospital.hospital_type =hospital_type
                    
                    specializations.specialization_name=specialization_name
                    services.service_name = service_name
                    departments.hospital_department_name = department_name 

                    hospital.save()
                    specializations.save()
                    services.save()
                    departments.save()
                    return redirect('hospital-list')

             context = { 'admin': user,'hospital':hospital,'departments':departments,'specializations':specializations,'services':services}
             return render(request, 'hospital_admin/edit-hospital.html',context)

@login_required(login_url='admin-login')
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

@login_required(login_url='admin-login')
def delete_hospital(request, pk):
	hospital = Hospital_Information.objects.get(hospital_id=pk)
	hospital.delete()
	return redirect('hospital-list')

@login_required(login_url='admin-login')
def generate_random_invoice():
    N = 4
    string_var = ""
    string_var = ''.join(random.choices(string.digits, k=N))
    string_var = "#INV-" + string_var
    return string_var


@login_required(login_url='admin-login')
def create_invoice(request, pk):
    if  request.user.is_hospital_admin:
        user = Admin_Information.objects.get(user=request.user)

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

    context = {'patient': patient,'admin': user}
    return render(request, 'hospital_admin/create-invoice.html', context)

@login_required(login_url='admin-login')
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

@login_required(login_url='admin-login')
def add_pharmacist(request):
    if request.user.is_hospital_admin:
     user = Admin_Information.objects.get(user=request.user)
    return render(request, 'hospital_admin/add-pharmacist.html',{'admin': user})  

