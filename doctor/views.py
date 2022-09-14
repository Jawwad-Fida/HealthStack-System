import email
from multiprocessing import context
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import DoctorUserCreationForm, DoctorForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import cache_control
from hospital.models import User, Patient
from hospital_admin.models import Admin_Information,Clinical_Laboratory_Technician
from .models import Doctor_Information, Appointment, Education, Experience, Prescription_medicine, Report,Specimen,Test, Prescription_test, Prescription

from django.db.models import Q, Count
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
import random
import string
from datetime import datetime, timedelta
import datetime
import re

from django.core.mail import BadHeaderError, send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.html import strip_tags

from io import BytesIO
from urllib import response
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from .models import Report

# Create your views here.

def generate_random_string():
    N = 8
    string_var = ""
    string_var = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=N))
    return string_var

@login_required(login_url="doctor-login")
def doctor_change_password(request,pk):
    doctor = Doctor_Information.objects.get(user_id=pk)
    context={'doctor':doctor}
    if request.method == "POST":
        
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]
        if new_password == confirm_password:
            
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request,"Password Changed Successfully")
            return redirect("doctor-dashboard")
            
        else:
            messages.error(request,"New Password and Confirm Password is not same")
            return redirect("change-password",pk)
    return render(request, 'doctor-change-password.html',context)

@login_required(login_url="doctor-login")
def schedule_timings(request):
    doctor = Doctor_Information.objects.get(user=request.user)
    context = {'doctor': doctor}
    
    return render(request, 'schedule-timings.html', context)

@login_required(login_url="doctor-login")
def patient_id(request):
    return render(request, 'patient-id.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutDoctor(request):
    user = User.objects.get(id=request.user.id)
    if user.is_doctor:
        user.login_status == "offline"
        user.save()
        logout(request)
    
    messages.info(request, 'User Logged out')
    return render(request,'doctor-login.html')


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
                # user.login_status = "online"
                # user.save()
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

@login_required(login_url="doctor-login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def doctor_dashboard(request):
        if request.user.is_authenticated:    
            if request.user.is_doctor:
                # doctor = Doctor_Information.objects.get(user_id=pk)
                doctor = Doctor_Information.objects.get(user=request.user)
                # appointments = Appointment.objects.filter(doctor=doctor).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed'))
                
                current_date = datetime.date.today()
                current_date_str = str(current_date)  
                today_appointments = Appointment.objects.filter(date=current_date_str).filter(doctor=doctor).filter(appointment_status='confirmed')
                
                next_date = current_date + datetime.timedelta(days=1) # next days date 
                next_date_str = str(next_date)  
                next_days_appointment = Appointment.objects.filter(date=next_date_str).filter(doctor=doctor).filter(appointment_status='pending').count()
                
                today_patient_count = Appointment.objects.filter(date=current_date_str).filter(doctor=doctor).annotate(count=Count('patient'))
                total_appointments_count = Appointment.objects.filter(doctor=doctor).annotate(count=Count('id'))
            else:
                return redirect('doctor-logout')
            
            context = {'doctor': doctor, 'today_appointments': today_appointments, 'today_patient_count': today_patient_count, 'total_appointments_count': total_appointments_count, 'next_days_appointment': next_days_appointment, 'current_date': current_date_str, 'next_date': next_date_str}
            return render(request, 'doctor-dashboard.html', context)
        else:
            return redirect('doctor-login')
 
 
@login_required(login_url="doctor-login")
def appointments(request):
    doctor = Doctor_Information.objects.get(user=request.user)

    appointments = Appointment.objects.filter(doctor=doctor).filter(appointment_status='pending').order_by('date')
    context = {'doctor': doctor, 'appointments': appointments}
    return render(request, 'appointments.html', context) 
 
        
@login_required(login_url="doctor-login")
def accept_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.appointment_status = 'confirmed'
    appointment.save()
    
    # Mailtrap
    
    patient_email = appointment.patient.email
    patient_name = appointment.patient.name
    patient_username = appointment.patient.username
    patient_serial_number = appointment.patient.serial_number
    doctor_name = appointment.doctor.name

    appointment_serial_number = appointment.serial_number
    appointment_date = appointment.date
    appointment_time = appointment.time
    appointment_status = appointment.appointment_status
    
    subject = "Appointment Acceptance Email"
    
    values = {
            "email":patient_email,
            "name":patient_name,
            "username":patient_username,
            "serial_number":patient_serial_number,
            "doctor_name":doctor_name,
            "appointment_serial_num":appointment_serial_number,
            "appointment_date":appointment_date,
            "appointment_time":appointment_time,
            "appointment_status":appointment_status,
    }
    
    html_message = render_to_string('appointment_accept_mail.html', {'values': values})
    plain_message = strip_tags(html_message)
    
    try:
        send_mail(subject, plain_message, 'hospital_admin@gmail.com',  [patient_email], html_message=html_message, fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found')
    
    return redirect('doctor-dashboard')

@login_required(login_url="doctor-login")
def reject_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.appointment_status = 'cancelled'
    appointment.save()
    
    # Mailtrap
    
    patient_email = appointment.patient.email
    patient_name = appointment.patient.name
    doctor_name = appointment.doctor.name

    subject = "Appointment Rejection Email"
    
    values = {
            "email":patient_email,
            "name":patient_name,
            "doctor_name":doctor_name,
    }
    
    html_message = render_to_string('appointment_reject_mail.html', {'values': values})
    plain_message = strip_tags(html_message)
    
    try:
        send_mail(subject, plain_message, 'hospital_admin@gmail.com',  [patient_email], html_message=html_message, fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found')
    
    
    return redirect('doctor-dashboard')



#         end_year = doctor.end_year
#         end_year = re.sub("'", "", end_year)
#         end_year = end_year.replace("[", "")
#         end_year = end_year.replace("]", "")
#         end_year = end_year.replace(",", "")
#         end_year_array = end_year.split()       
#         experience = zip(work_place_array, designation_array, start_year_array, end_year_array)


@login_required(login_url="doctor-login")
def doctor_profile(request, pk):
    # request.user --> get logged in user
    if request.user.is_patient:
        patient = request.user.patient
    else:
        patient = None
    
    doctor = Doctor_Information.objects.get(doctor_id=pk)
    # doctor = Doctor_Information.objects.filter(doctor_id=pk).order_by('-doctor_id')
    
    educations = Education.objects.filter(doctor=doctor).order_by('-year_of_completion')
    experiences = Experience.objects.filter(doctor=doctor).order_by('-from_year','-to_year')
            
    context = {'doctor': doctor, 'patient': patient, 'educations': educations, 'experiences': experiences}
    return render(request, 'doctor-profile.html', context)

@login_required(login_url="doctor-login")
def delete_education(request, pk):
    if request.user.is_doctor:
        doctor = Doctor_Information.objects.get(user=request.user)
        
        educations = Education.objects.get(education_id=pk)
        educations.delete()
        return redirect('doctor-profile-settings')

     
@login_required(login_url="doctor-login")
def delete_experience(request, pk):
    if request.user.is_doctor:
        doctor = Doctor_Information.objects.get(user=request.user)
        
        experiences = Experience.objects.get(experience_id=pk)
        experiences.delete()
        return redirect('doctor-profile-settings')
      
            
#             if degree:
#                 degree = re.sub("'", "", degree)
#                 degree = degree.replace("[", "")
#                 degree = degree.replace("]", "")
#                 degree = degree.replace(",", "")
#                 degree_array = degree.split()
      
        
@login_required(login_url="doctor-login")
def doctor_profile_settings(request):
    # profile_Settings.js
    if request.user.is_doctor:
        doctor = Doctor_Information.objects.get(user=request.user)
        old_featured_image = doctor.featured_image
        
        #Education, Experience

        if request.method == 'GET':
            educations = Education.objects.filter(doctor=doctor)
            experiences = Experience.objects.filter(doctor=doctor)
            
                
            context = {'doctor': doctor, 'educations': educations, 'experiences': experiences}
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
            nid = request.POST.get('nid')
            visit_hour = request.POST.get('visit_hour')
            
            degree = request.POST.getlist('degree')
            institute = request.POST.getlist('institute')
            year_complete = request.POST.getlist('year_complete')
            hospital_name = request.POST.getlist('hospital_name')     
            start_year= request.POST.getlist('from')
            end_year = request.POST.getlist('to')
            designation = request.POST.getlist('designation')

            doctor.name = name
            doctor.visiting_hour = visit_hour
            doctor.nid = nid
            doctor.gender = gender
            doctor.featured_image = featured_image
            doctor.phone_number = number
            #doctor.visiting_hour
            doctor.consultation_fee = consultation_fee
            doctor.report_fee = report_fee
            doctor.description = description
            doctor.dob = dob
            
            doctor.save()
            
            # Education
            for i in range(len(degree)):
                education = Education(doctor=doctor)
                education.degree = degree[i]
                education.institute = institute[i]
                education.year_of_completion = year_complete[i]
                education.save()

            # Experience
            for i in range(len(hospital_name)):
                experience = Experience(doctor=doctor)
                experience.work_place_name = hospital_name[i]
                experience.from_year = start_year[i]
                experience.to_year = end_year[i]
                experience.designation = designation[i]
                experience.save()
      
            # context = {'degree': degree}
            return redirect('doctor-dashboard')
    else:
        redirect('doctor-logout')
               
        
@login_required(login_url="doctor-login")      
def booking_success(request):
    return render(request, 'booking-success.html')

@login_required(login_url="doctor-login")
def booking(request, pk):
    patient = request.user.patient
    doctor = Doctor_Information.objects.get(doctor_id=pk)

    if request.method == 'POST':
        appointment = Appointment(patient=patient, doctor=doctor)
        date = request.POST['appoint_date']
        time = request.POST['appoint_time']
        appointment_type = request.POST['appointment_type']

    
        transformed_date = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
        transformed_date = str(transformed_date)
         
        appointment.date = transformed_date
        appointment.time = time
        appointment.appointment_status = 'pending'
        appointment.serial_number = generate_random_string()
        appointment.appointment_type = appointment_type
        appointment.save()
        return redirect('patient-dashboard')

    context = {'patient': patient, 'doctor': doctor}
    return render(request, 'booking.html', context)


@login_required(login_url="doctor-login")
def my_patients(request):
    if request.user.is_doctor:
        doctor = Doctor_Information.objects.get(user=request.user)
        appointments = Appointment.objects.filter(doctor=doctor)
        # patients = Patient.objects.all()
    else:
        redirect('doctor-logout')
    
    
    context = {'doctor': doctor, 'appointments': appointments}
    return render(request, 'my-patients.html', context)


# def patient_profile(request):
#     return render(request, 'patient_profile.html')
@login_required(login_url="doctor-login")
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






@login_required(login_url="doctor-login")
def create_prescription(request,pk):
        if request.user.is_doctor:
            doctor = Doctor_Information.objects.get(user=request.user)
            patient = Patient.objects.get(patient_id=pk) 
            create_date = datetime.date.today()
            
            if request.method == 'POST':
                prescription = Prescription(doctor=doctor, patient=patient)
                
                test_name= request.POST.getlist('test_name')
                test_description = request.POST.getlist('description')
                medicine_name = request.POST.getlist('medicine_name')
                medicine_quantity = request.POST.getlist('quantity')
                medecine_frequency = request.POST.getlist('frequency')
                medicine_duration = request.POST.getlist('duration')
                medicine_relation_with_meal = request.POST.getlist('relation_with_meal')
                medicine_instruction = request.POST.getlist('instruction')
                extra_information = request.POST.get('extra_information')

            
                prescription.extra_information = extra_information
                prescription.create_date = create_date
                prescription.save()

                for i in range(len(medicine_name)):
                    medicine = Prescription_medicine(prescription=prescription)
                    medicine.medicine_name = medicine_name[i]
                    medicine.quantity = medicine_quantity[i]
                    medicine.frequency = medecine_frequency[i]
                    medicine.duration = medicine_duration[i]
                    medicine.instruction = medicine_instruction[i]
                    medicine.relation_with_meal = medicine_relation_with_meal[i]
                    medicine.save()

                for i in range(len(test_name)):
                    tests = Prescription_test(prescription=prescription)
                    tests.test_name = test_name[i]
                    tests.test_description = test_description[i]
                    tests.save()

                return redirect('patient-profile', pk=patient.patient_id)
             
        context = {'doctor': doctor,'patient': patient}  
        return render(request, 'create-prescription.html',context)

       

def render_to_pdf(template_src, context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type="aplication/pdf")
    return None




def report_pdf(request, pk):
 if request.user.is_patient:
    patient = Patient.objects.get(user=request.user)
    report = Report.objects.get(report_id=pk)
    specimen = Specimen.objects.filter(report=report)
    test = Test.objects.filter(report=report)
    # current_date = datetime.date.today()
    context={'patient':patient,'report':report,'test':test,'specimen':specimen}
    pdf=render_to_pdf('report_pdf.html', context)
    if pdf:
        response=HttpResponse(pdf, content_type='application/pdf')
        content="inline; filename=report.pdf"
        # response['Content-Disposition']= content
        return response
    return HttpResponse("Not Found")


# def testing(request):
#     doctor = Doctor_Information.objects.get(user=request.user)
#     degree = doctor.degree
#     degree = re.sub("'", "", degree)
#     degree = degree.replace("[", "")
#     degree = degree.replace("]", "")
#     degree = degree.replace(",", "")
#     degree_array = degree.split()
    
#     education = zip(degree_array, institute_array)
    
#     context = {'doctor': doctor, 'degree': institute, 'institute_array': institute_array, 'education': education}
#     # test range, len, and loop to show variables before moving on to doctor profile
    
#     return render(request, 'testing.html', context)


@login_required(login_url="login")
def patient_search(request, pk):
    if request.user.is_authenticated and request.user.is_doctor:
        doctor = Doctor_Information.objects.get(doctor_id=pk)
        id = int(request.GET['search_query'])
        patient = Patient.objects.get(patient_id=id)
        appointments = Appointment.objects.filter(doctor=doctor).filter(patient=patient)
        context = {'patient': patient, 'doctor': doctor, 'appointments': appointments}
        return render(request, 'patient-profile.html', context)
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'doctor-login.html')






@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):    
    user.login_status = True
    user.save()

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):   
    user.login_status = False
    user.save()
