import email
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

import doctor
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, PatientForm
from hospital.models import Hospital_Information, User, Patient

from hospital_admin.models import hospital_department, specialization, service


from django.views.decorators.cache import cache_control


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
import datetime


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from doctor.models import Prescription


from .utils import searchDoctors, searchHospitals, searchDepartmentDoctors


# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver

from .models import Patient, User

from doctor.models import Doctor_Information, Appointment,Report, Specimen, Test, Prescription, Perscription_medicine, Perscription_test

from sslcommerz.models import Payment
from django.db.models import Q, Count
import re

from io import BytesIO
from urllib import response
from django.shortcuts import render

from django.http import HttpResponse


from doctor.models import  Prescription,Perscription_medicine,Perscription_test
from hospital.models import Patient
from datetime import datetime


# Create your views here.

# function to return views for the urls


def hospital_home(request):
    doctors = Doctor_Information.objects.filter(register_status='Accepted')
    context = {'doctors': doctors} 
    return render(request, 'index-2.html', context)

@login_required(login_url="login")

def change_password(request,pk):
    patient = Patient.objects.get(user_id=pk)
    context={"patient":patient}
    if request.method == "POST":
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]
        if new_password == confirm_password:
            
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request,"Password Changed Successfully")
            return redirect("patient-dashboard")
            
        else:
            messages.error(request,"New Password and Confirm Password is not same")
            return redirect("change-password",pk)
    return render(request, 'change-password.html',context)



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


# def multiple_hospital(request):
#     return render(request, 'multiple-hospital.html')
@login_required(login_url="login")
def chat(request, pk):
    patient = Patient.objects.get(user_id=pk)
    doctors = Doctor_Information.objects.all()

    context = {'patient': patient, 'doctors': doctors}
    return render(request, 'chat.html', context)

@login_required(login_url="login")
def chat_doctor(request):
    if request.user.is_doctor:
        doctor = Doctor_Information.objects.get(user=request.user)
        patients = Patient.objects.all()
        
    context = {'patients': patients, 'doctor': doctor}
    return render(request, 'chat-doctor.html', context)

        
@login_required(login_url="login")
def pharmacy_shop(request):
    return render(request, 'pharmacy/shop.html')


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
            if request.user.is_patient:          
                return redirect('patient-dashboard')
            else:
                messages.error(request, 'Invalid credentials. Not a Patient')
                return redirect('logout')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'patient-login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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


@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def patient_dashboard(request):
    if request.user.is_patient:
        patient = Patient.objects.get(user=request.user)
        report = Report.objects.filter(patient=patient)
        # patient = Patient.objects.get(user_id=pk)
        # appointments = Appointment.objects.filter(patient=patient)
        appointments = Appointment.objects.filter(patient=patient).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed'))
        payments = Payment.objects.filter(patient=patient).filter(appointment__in=appointments).filter(payment_type='appointment')

        context = {'patient': patient, 'appointments': appointments, 'payments': payments,'report':report}
    else:
        return redirect('logout')
        
    return render(request, 'patient-dashboard.html', context)


# def profile_settings(request):
#     if request.user.is_patient:
#         # patient = Patient.objects.get(user_id=pk)
#         patient = Patient.objects.get(user=request.user)
#         form = PatientForm(instance=patient)  

#         if request.method == 'POST':
#             form = PatientForm(request.POST, request.FILES,instance=patient)  
#             if form.is_valid():
#                 form.save()
#                 return redirect('patient-dashboard')
#             else:
#                 form = PatientForm()
#     else:
#         redirect('logout')

#     context = {'patient': patient, 'form': form}
#     return render(request, 'profile-settings.html', context)


@login_required(login_url="login")
def profile_settings(request):
    if request.user.is_patient:
        # patient = Patient.objects.get(user_id=pk)
        patient = Patient.objects.get(user=request.user)
        old_featured_image = patient.featured_image
        
        if request.method == 'GET':
            context = {'patient': patient}
            return render(request, 'profile-settings.html', context)
        elif request.method == 'POST':
            if 'featured_image' in request.FILES:
                featured_image = request.FILES['featured_image']
            else:
                featured_image = old_featured_image
                
            name = request.POST.get('name')
            dob = request.POST.get('dob')
            age = request.POST.get('age')
            blood_group = request.POST.get('blood_group')
            phone_number = request.POST.get('phone_number')
            address = request.POST.get('address')
            nid = request.POST.get('nid')
            history = request.POST.get('history')
            
            patient.name = name
            patient.age = age
            patient.phone_number = phone_number
            patient.address = address
            patient.blood_group = blood_group
            patient.history = history
            patient.dob = dob
            patient.nid = nid
            patient.featured_image = featured_image
            
            patient.save()
            return redirect('patient-dashboard')
    else:
        redirect('logout')  

@login_required(login_url="login")
def search(request):
    if request.user.is_authenticated and request.user.is_patient:
        # patient = Patient.objects.get(user_id=pk)
        
        patient = Patient.objects.get(user=request.user)
        doctors = Doctor_Information.objects.filter(register_status='Accepted')
        
        doctors, search_query = searchDoctors(request)
        # context = {'patient': patient, 'doctors': doctors, 'profiles': profiles, 'search_query': search_query}
        context = {'patient': patient, 'doctors': doctors, 'search_query': search_query}
        return render(request, 'search.html', context)
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'patient-login.html')    
    

def checkout_payment(request):
    return render(request, 'checkout.html')

@login_required(login_url="login")
def multiple_hospital(request):
    
    if request.user.is_authenticated: 
        
        if request.user.is_patient:
            # patient = Patient.objects.get(user_id=pk)
            patient = Patient.objects.get(user=request.user)
            doctors = Doctor_Information.objects.all()
            hospitals = Hospital_Information.objects.all()
            
            hospitals, search_query = searchHospitals(request)
        
            context = {'patient': patient, 'doctors': doctors, 'hospitals': hospitals, 'search_query': search_query}
            return render(request, 'multiple-hospital.html', context)
        
        elif request.user.is_doctor:
            doctor = Doctor_Information.objects.get(user=request.user)
            hospitals = Hospital_Information.objects.all()
            
            hospitals, search_query = searchHospitals(request)
            
            context = {'doctor': doctor, 'hospitals': hospitals, 'search_query': search_query}
            return render(request, 'multiple-hospital.html', context)
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'patient-login.html') 
    
    
@login_required(login_url="login")
def hospital_profile(request, pk):
    
    if request.user.is_authenticated: 
        
        if request.user.is_patient:
            patient = Patient.objects.get(user=request.user)
            doctors = Doctor_Information.objects.all()
            hospitals = Hospital_Information.objects.get(hospital_id=pk)
        
            departments = hospital_department.objects.filter(hospital=hospitals)
            specializations = specialization.objects.filter(hospital=hospitals)
            services = service.objects.filter(hospital=hospitals)
            
            # department_list = None
            # for d in departments:
            #     vald = d.hospital_department_name
            #     vald = re.sub("'", "", vald)
            #     vald = vald.replace("[", "")
            #     vald = vald.replace("]", "")
            #     vald = vald.replace(",", "")
            #     department_list = vald.split()
                
            
            context = {'patient': patient, 'doctors': doctors, 'hospitals': hospitals, 'departments': departments, 'specializations': specializations, 'services': services}
            return render(request, 'hospital-profile.html', context)
        
        elif request.user.is_doctor:
           
            doctor = Doctor_Information.objects.get(user=request.user)
            hospitals = Hospital_Information.objects.get(hospital_id=pk)
            
            departments = hospital_department.objects.filter(hospital=hospitals)
            specializations = specialization.objects.filter(hospital=hospitals)
            services = service.objects.filter(hospital=hospitals)
            
            
            context = {'doctor': doctor, 'hospitals': hospitals, 'departments': departments, 'specializations': specializations, 'services': services}
            return render(request, 'hospital-profile.html', context)
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'patient-login.html') 
    
    
def data_table(request):
    return render(request, 'data-table.html')


def hospital_department_list(request, pk):
    if request.user.is_authenticated: 
        
        if request.user.is_patient:
            # patient = Patient.objects.get(user_id=pk)
            patient = Patient.objects.get(user=request.user)
            doctors = Doctor_Information.objects.all()
            
            hospitals = Hospital_Information.objects.get(hospital_id=pk)
            departments = hospital_department.objects.filter(hospital=hospitals)
            
            # hospitals, search_query = searchHospitals(request)
        
            context = {'patient': patient, 'doctors': doctors, 'hospitals': hospitals, 'departments': departments}
            return render(request, 'hospital-department.html', context)
        
        elif request.user.is_doctor:
            doctor = Doctor_Information.objects.get(user=request.user)
            hospitals = Hospital_Information.objects.get(hospital_id=pk)
            departments = hospital_department.objects.filter(hospital=hospitals)
            
            # hospitals, search_query = searchHospitals(request)
            
            context = {'doctor': doctor, 'hospitals': hospitals, 'departments': departments}
            return render(request, 'hospital-department.html', context)
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'patient-login.html')


def hospital_doctor_list(request, pk):
    if request.user.is_authenticated and request.user.is_patient:
        # patient = Patient.objects.get(user_id=pk)
        
        patient = Patient.objects.get(user=request.user)
              
        departments = hospital_department.objects.get(hospital_department_id=pk)
        doctors = Doctor_Information.objects.filter(department_name=departments)
        
        doctors, search_query = searchDepartmentDoctors(request, pk)
        
        context = {'patient': patient, 'department': departments, 'doctors': doctors, 'search_query': search_query, 'pk_id': pk}
        return render(request, 'hospital-doctor-list.html', context)

    elif request.user.is_authenticated and request.user.is_doctor:
        # patient = Patient.objects.get(user_id=pk)
        
        doctor = Doctor_Information.objects.get(user=request.user)
        departments = hospital_department.objects.get(hospital_department_id=pk)
        
        doctors = Doctor_Information.objects.filter(department_name=departments)
        doctors, search_query = searchDepartmentDoctors(request, pk)
        

        context = {'doctor':doctor, 'department': departments, 'doctors': doctors, 'search_query': search_query, 'pk_id': pk}
        return render(request, 'hospital-doctor-list.html', context)
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'patient-login.html')   

def hospital_doctor_register(request, pk):
    if request.user.is_authenticated: 
        
        if request.user.is_doctor:
            doctor = Doctor_Information.objects.get(user=request.user)
            hospitals = Hospital_Information.objects.get(hospital_id=pk)
            
            departments = hospital_department.objects.filter(hospital=hospitals)
            specializations = specialization.objects.filter(hospital=hospitals)
            
            if request.method == 'POST':
                if 'certificate_image' in request.FILES:
                    certificate_image = request.FILES['certificate_image']
                else:
                    certificate_image = "doctors_certificate/default.png"
                
                department_id_selected = request.POST.get('department_radio')
                specialization_id_selected = request.POST.get('specialization_radio')
                
                department_chosen = hospital_department.objects.get(hospital_department_id=department_id_selected)
                specialization_chosen = specialization.objects.get(specialization_id=specialization_id_selected)
                
                doctor.department_name = department_chosen
                doctor.specialization = specialization_chosen
                doctor.register_status = 'Pending'
                doctor.certificate_image = certificate_image
                
                doctor.save()
                
                return redirect('doctor-dashboard')
                
                 
            context = {'doctor': doctor, 'hospitals': hospitals, 'departments': departments, 'specializations': specializations}
            return render(request, 'hospital-doctor-register.html', context)
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'doctor-login.html')
    
    
def testing(request):
    # hospitals = Hospital_Information.objects.get(hospital_id=1)
        
    # departments = hospital_department.objects.filter(hospital=hospitals)
    # specializations = specialization.objects.filter(hospital=hospitals)
    # services = service.objects.filter(hospital=hospitals)
    
    # department_list = None
    # for d in departments:
    #     vald = d.hospital_department_name
    #     vald = re.sub("'", "", vald)
    #     vald = vald.replace("[", "")
    #     vald = vald.replace("]", "")
    #     vald = vald.replace(",", "")
    #     department_list = vald.split()
    #     # department_list.append(d.hospital_department_name)
    
    # # education = zip(degree_array, institute_array)

    
    # given_date = "09/08/2022"
    # transformed_date = datetime.datetime.strptime(given_date, '%m/%d/%Y').strftime('%Y-%m-%d')
    # transformed_date = str(transformed_date)
    

    sat_date = datetime.date.today()
    sat_date_str = str(sat_date)
    sat = sat_date.strftime("%A")

    sun_date = sat_date + datetime.timedelta(days=1) 
    sun_date_str = str(sun_date)
    sun = sun_date.strftime("%A")
    
    mon_date = sat_date + datetime.timedelta(days=2) 
    mon_date_str = str(mon_date)
    mon = mon_date.strftime("%A")
    
    tues_date = sat_date + datetime.timedelta(days=3) 
    tues_date_str = str(tues_date)
    tues = tues_date.strftime("%A")
    
    wed_date = sat_date + datetime.timedelta(days=4) 
    wed_date_str = str(wed_date)
    wed = wed_date.strftime("%A")
    
    thurs_date = sat_date + datetime.timedelta(days=5) 
    thurs_date_str = str(thurs_date)
    thurs = thurs_date.strftime("%A")
    
    fri_date = sat_date + datetime.timedelta(days=6) 
    fri_date_str = str(fri_date)
    fri = fri_date.strftime("%A")
    
    
    day = datetime.date.today().strftime("%A")  

    sat_count = Appointment.objects.filter(date=sat_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
    sun_count = Appointment.objects.filter(date=sun_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
    mon_count = Appointment.objects.filter(date=mon_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
    tues_count = Appointment.objects.filter(date=tues_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
    wed_count = Appointment.objects.filter(date=wed_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
    thurs_count = Appointment.objects.filter(date=thurs_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
    fri_count = Appointment.objects.filter(date=fri_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
    
    
    context = {'sat_count': sat_count, 'sun_count': sun_count, 'mon_count': mon_count, 'tues_count': tues_count, 'wed_count': wed_count, 'thurs_count': thurs_count, 'fri_count': fri_count, 'sat': sat, 'sun': sun, 'mon': mon, 'tues': tues, 'wed': wed, 'thurs': thurs, 'fri': fri}
    # test range, len, and loop to show variables before moving on to doctor profile
    
    return render(request, 'testing.html', context)

def view_report(request,pk):
    if request.user.is_patient:
        patient = Patient.objects.get(user=request.user)
        report = Report.objects.filter(report_id=pk)
        specimen = Specimen.objects.filter(report__in=report)
        test = Test.objects.filter(report__in=report)

        current_date = datetime.date.today()

        context = {'patient':patient,'current_date' : current_date,'report':report,'test':test,'specimen':specimen}
        return render(request, 'view-report.html',context)
    else:
        redirect('logout') 


def test_cart(request):
    return render(request, 'test-cart.html')


def prescription_view(request):
    #  if request.user.is_patient:
    #     patient = Patient.objects.get(user=request.user)
    #     prescription = Prescription.objects.filter(prescription_id=pk)
    #     perscription_medicine = Perscription_medicine.objects.filter(prescription__in=prescription)
    #     prescription_test = Perscription_test.objects.filter(prescription__in=prescription)

    #     current_date = datetime.date.today()

        # context = {'patient':patient, 'current_date' : current_date, 'prescription':prescription,'prescription_test':prescription_test,'perscription_medicine':perscription_medicine}
    return render(request, 'prescription-view.html')
    #  else:
    #     redirect('logout') 


# def render_to_pdf(template_src, context_dict={}):
#     template=get_template(template_src)
#     html=template.render(context_dict)
#     result=BytesIO()
#     pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(),content_type="aplication/pdf")
#     return None




# def prescription_pdf(request,pk):
#  if request.user.is_patient:
#     patient = Patient.objects.get(user=request.user)
#     prescription = Prescription.objects.get(prescription_id=pk)
#     perscription_medicine = Perscription_medicine.objects.filter(prescription=prescription)
#     perscription_test = Perscription_test.objects.filter(prescription=prescription)
#     current_date = datetime.date.today()
#     context={'patient':patient,'current_date' : current_date,'prescription':prescription,'perscription_test':perscription_test,'perscription_medicine':perscription_medicine}
#     pdf=render_to_pdf('prescription_pdf.html', context)
#     if pdf:
#         response=HttpResponse(pdf, content_type='application/pdf')
#         content="inline; filename=report.pdf"
#         # response['Content-Disposition']= content
#         return response
#     return HttpResponse("Not Found")