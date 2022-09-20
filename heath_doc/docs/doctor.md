# Welcome to Doctor

We have developed a convenient doctor/patient interface to bring you a service that allows you to have a medical consultation.

##  The main duties of a Doctor :

- Accept or  appointments from patients.
- View patient profile after accepting appointments.
- Can register himself to a specific hospital.
- Search patients.
- Create prescription.
- Sending mail to the patient about appointment confirmation.
- Chat with patient.
- Doctor Profile settings.



## Accepting Appointments of patients
```python
def accept_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.appointment_status = 'confirmed'
    appointment.save()

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
    
    messages.success(request, 'Appointment Accepted')
    
    return redirect('doctor-dashboard')
```

## Doctor Dashboard 
![title](doctor/Screenshot (218).png)

## Doctor Profile
![title](doctor/Screenshot (219).png)

## Search Hospital
![title](doctor/Screenshot (220).png)

## Search Patients

```python
def patient_search(request, pk):
    if request.user.is_authenticated and request.user.is_doctor:
        doctor = Doctor_Information.objects.get(doctor_id=pk)
        id = int(request.GET['search_query'])
        patient = Patient.objects.get(patient_id=id)
        prescription = Prescription.objects.filter(doctor=doctor).filter(patient=patient)
        context = {'patient': patient, 'doctor': doctor, 'prescription': prescription}
        return render(request, 'patient-profile.html', context)
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'doctor-login.html')

```

## Create Prescription
```python
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
                test_info_id = request.POST.getlist('id')

            
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
                    tests.test_info_id = test_info_id[i]
                    test_info = Test_Information.objects.get(test_id=test_info_id[i])
                    tests.test_info_price = test_info.test_price
                   
                    tests.save()

                messages.success(request, 'Prescription Created')
                return redirect('patient-profile', pk=patient.patient_id)
             
        context = {'doctor': doctor,'patient': patient}  
        return render(request, 'create-prescription.html',context)
```

## Profile Settings

![title](doctor/Screenshot (223).png)
