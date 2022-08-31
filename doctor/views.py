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

from django.db.models import Q, Count

import random
import string

from datetime import datetime, timedelta
import datetime

# import json
import re

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
        
        # 
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
                
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            if request.user.is_doctor:
                return redirect('doctor-dashboard')
            else:
                messages.error(request, 'Invalid credentials. Not a Doctor')
                return redirect('doctor-logout')   
        else:
            messages.error(request, 'Invalid username or password')  
        # else:
        #     messages.error(request, 'Invalid credentials. Not a Doctor')
        #     return redirect('doctor-login')
            

    return render(request, 'doctor-login.html')


def doctor_dashboard(request):
    if request.user.is_doctor:
        # doctor = Doctor_Information.objects.get(user_id=pk)
        doctor = Doctor_Information.objects.get(user=request.user)
        patient = Patient.objects.all()
        appointments = Appointment.objects.filter(doctor=doctor).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed'))
        current_date = datetime.date.today()
        today_appointments = Appointment.objects.filter(date=current_date).filter(doctor=doctor).filter(appointment_status='confirmed')
        
        # next days date
        next_date = current_date + datetime.timedelta(days=1)
        
        # Count
        next_days_appointment = Appointment.objects.filter(date=next_date).filter(doctor=doctor).filter(appointment_status='pending').count()
        # .values('count')
        today_patient_count = Appointment.objects.filter(date=current_date).filter(doctor=doctor).annotate(count=Count('patient'))
        total_appointments_count = Appointment.objects.filter(doctor=doctor).annotate(count=Count('id'))
    else:
        redirect('doctor-logout')
    
    context = {'doctor': doctor, 'appointments': appointments, 'today_appointments': today_appointments, 'today_patient_count': today_patient_count, 'total_appointments_count': total_appointments_count, 'next_days_appointment': next_days_appointment, 'current_date': current_date, 'next_date': next_date}
    return render(request, 'doctor-dashboard.html', context)

def accept_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.appointment_status = 'confirmed'
    appointment.save()
    return redirect('doctor-dashboard')

def reject_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.appointment_status = 'cancelled'
    appointment.save()
    return redirect('doctor-dashboard')

# def doctor_profile_settings(request):

#     if request.user.is_doctor:
#         doctor = Doctor_Information.objects.get(user=request.user)
    
#         form = DoctorForm(instance=doctor)

#         if request.method == 'POST':
#             form = DoctorForm(request.POST, request.FILES,instance=doctor)
#             if form.is_valid():
#                 form.save()
#                 return redirect('doctor-dashboard')
#             else:
#                 form = DoctorForm()
#     else:
#         redirect('doctor-logout')

#     context = {'doctor': doctor, 'form': form}
#     return render(request, 'doctor-profile-settings.html', context)

def doctor_profile(request, pk):
    # request.user --> get logged in user
    if request.user.is_patient:
        patient = request.user.patient
    else:
        patient = None
    
    doctor = Doctor_Information.objects.get(doctor_id=pk)
    # doctor = Doctor_Information.objects.filter(doctor_id=pk).order_by('-doctor_id')
    
    degree = doctor.degree
    work_place = doctor.work_place
    
    
    education = None
    experience = None
    
    
    if degree:
        degree = re.sub("'", "", degree)
        degree = degree.replace("[", "")
        degree = degree.replace("]", "")
        degree = degree.replace(",", "")
        degree_array = degree.split()
        
        institute = doctor.institute
        institute = re.sub("'", "", institute)
        institute = institute.replace("[", "")
        institute = institute.replace("]", "")
        institute = institute.replace(",", "")
        institute_array = institute.split()
        
        completion_year = doctor.completion_year
        completion_year = re.sub("'", "", completion_year)
        completion_year = completion_year.replace("[", "")
        completion_year = completion_year.replace("]", "")
        completion_year = completion_year.replace(",", "")
        completion_year_array = completion_year.split()
    
        education = zip(degree_array, institute_array, completion_year_array)
    else:
        education = None
        
    if work_place:
        work_place = re.sub("'", "", work_place)
        work_place = work_place.replace("[", "")
        work_place = work_place.replace("]", "")
        work_place = work_place.replace(",", "")
        work_place_array = work_place.split()
        
        designation = doctor.designation
        designation = re.sub("'", "", designation)
        designation = designation.replace("[", "")
        designation = designation.replace("]", "")
        designation = designation.replace(",", "")
        designation_array = designation.split()
        
        start_year = doctor.start_year
        start_year = re.sub("'", "", start_year)
        start_year = start_year.replace("[", "")
        start_year = start_year.replace("]", "")
        start_year = start_year.replace(",", "")
        start_year_array = start_year.split()
        
        end_year = doctor.end_year
        end_year = re.sub("'", "", end_year)
        end_year = end_year.replace("[", "")
        end_year = end_year.replace("]", "")
        end_year = end_year.replace(",", "")
        end_year_array = end_year.split()
                
                
        experience = zip(work_place_array, designation_array, start_year_array, end_year_array)
    else:
        experience = None
    
    context = {'doctor': doctor, 'patient': patient, 'education': education, 'experience': experience}
    
    return render(request, 'doctor-profile.html', context)

def doctor_profile_settings(request):
    # profile_Settings.js
    if request.user.is_doctor:
        doctor = Doctor_Information.objects.get(user=request.user)
        old_featured_image = doctor.featured_image
        
        education = None
        experience = None


        if request.method == 'GET':
            degree = doctor.degree
            work_place = doctor.work_place
            
            
            if degree:
                degree = re.sub("'", "", degree)
                degree = degree.replace("[", "")
                degree = degree.replace("]", "")
                degree = degree.replace(",", "")
                degree_array = degree.split()
                
                institute = doctor.institute
                institute = re.sub("'", "", institute)
                institute = institute.replace("[", "")
                institute = institute.replace("]", "")
                institute = institute.replace(",", "")
                institute_array = institute.split()
                
                completion_year = doctor.completion_year
                completion_year = re.sub("'", "", completion_year)
                completion_year = completion_year.replace("[", "")
                completion_year = completion_year.replace("]", "")
                completion_year = completion_year.replace(",", "")
                completion_year_array = completion_year.split()
                
                education = zip(degree_array, institute_array, completion_year_array)
            else:
                education = None
                
            if work_place:
                work_place = re.sub("'", "", work_place)
                work_place = work_place.replace("[", "")
                work_place = work_place.replace("]", "")
                work_place = work_place.replace(",", "")
                work_place_array = work_place.split()
                
                designation = doctor.designation
                designation = re.sub("'", "", designation)
                designation = designation.replace("[", "")
                designation = designation.replace("]", "")
                designation = designation.replace(",", "")
                designation_array = designation.split()
                
                start_year = doctor.start_year
                start_year = re.sub("'", "", start_year)
                start_year = start_year.replace("[", "")
                start_year = start_year.replace("]", "")
                start_year = start_year.replace(",", "")
                start_year_array = start_year.split()
                
                end_year = doctor.end_year
                end_year = re.sub("'", "", end_year)
                end_year = end_year.replace("[", "")
                end_year = end_year.replace("]", "")
                end_year = end_year.replace(",", "")
                end_year_array = end_year.split()
                
                
                experience = zip(work_place_array, designation_array, start_year_array, end_year_array)
            else:
                experience = None
                
                    
            context = {'doctor': doctor, 'education': education, 'experience': experience}
            return render(request, 'doctor-profile-settings.html', context)
        elif request.method == 'POST':
            if 'featured_image' in request.FILES:
                featured_image = request.FILES['featured_image']
            else:
                featured_image = old_featured_image
                
            name = request.POST.get('name')
            number = request.POST.get('number')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            description = request.POST.get('description')
            consultation_fee = request.POST.get('consultation_fee')
            report_fee = request.POST.get('report_fee')
            degree = request.POST.getlist('degree')
            institute = request.POST.getlist('institute')
            year_complete = request.POST.getlist('year_complete')
            hospital_name = request.POST.getlist('hospital_name')     
            start_year= request.POST.getlist('from')
            end_year = request.POST.getlist('to')
            designation = request.POST.getlist('designation')

            doctor.name = name
            doctor.gender = gender
            doctor.featured_image = featured_image
            doctor.phone_number = number
            #doctor.visiting_hour
            doctor.consultation_fee = consultation_fee
            doctor.report_fee = report_fee
            doctor.description = description
            doctor.dob = dob
            
            # Education
            doctor.institute = institute
            doctor.degree = degree
            doctor.completion_year = year_complete 
            
            # Experience
            doctor.work_place = hospital_name
            doctor.designation = designation
            doctor.start_year = start_year
            doctor.end_year = end_year
            
            doctor.save()
                
            # context = {'degree': degree}
            return redirect('doctor-dashboard')
    else:
        redirect('doctor-logout')
        
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

def patient_profile(request, pk):
    if request.user.is_doctor:
        # doctor = Doctor_Information.objects.get(user_id=pk)
        doctor = Doctor_Information.objects.get(user=request.user)
        patient = Patient.objects.get(patient_id=pk)
        appointments = Appointment.objects.filter(doctor=doctor).filter(patient=patient) 
    else:
        redirect('doctor-logout')
    context = {'doctor': doctor, 'appointments': appointments, 'patient': patient}  
    return render(request, 'patient-profile.html', context)

     
    
def testing(request):
    doctor = Doctor_Information.objects.get(user=request.user)
    degree = doctor.degree
    degree = re.sub("'", "", degree)
    degree = degree.replace("[", "")
    degree = degree.replace("]", "")
    degree = degree.replace(",", "")
    degree_array = degree.split()
    
    institute = doctor.institute
    institute = re.sub("'", "", institute)
    institute = institute.replace("[", "")
    institute = institute.replace("]", "")
    institute = institute.replace(",", "")
    institute_array = institute.split()


    education = zip(degree_array, institute_array)
    
    context = {'doctor': doctor, 'degree': institute, 'institute_array': institute_array, 'education': education}
    # test range, len, and loop to show variables before moving on to doctor profile
    
    return render(request, 'testing.html', context)

def chat_patient(request):
    if request.user.is_doctor:
        doctor = Doctor_Information.objects.get(user=request.user)
        patients = Patient.objects.all()
        
    context = {'patients': patients, 'doctor': doctor}
    return render(request, 'chat-patient.html', context)

def view_report(request):
    return render(request, 'view-report.html')

def add_report(request):
    return render(request, 'add-report.html')


def prescription_view(request):
    return render(request, 'prescription-view.html')

def create_prescription(request):
    return render(request, 'create-prescription.html')

