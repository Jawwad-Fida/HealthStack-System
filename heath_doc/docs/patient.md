# Welcome to Patient Dashboard

##  The main services a patient avail:

* `Visit multiple hospital, get emargency information of a hospital, and also gets doctor information.`
* `Search departmant`
* `Book doctor appointment`
* `Search Doctor `
* `View Prescription`
* `Book tests and pay online`
* `View Report history`
* `Profile edit`
* `Get mail for appointment and payment`
* `Medical Shop, Search Medicine, and buy Medicine`

## View hospital Information
```python
def hospital_profile(request, pk):
    
    if request.user.is_authenticated: 
        
        if request.user.is_patient:
            patient = Patient.objects.get(user=request.user)
            doctors = Doctor_Information.objects.all()
            hospitals = Hospital_Information.objects.get(hospital_id=pk)
        
            departments = hospital_department.objects.filter(hospital=hospitals)
            specializations = specialization.objects.filter(hospital=hospitals)
            services = service.objects.filter(hospital=hospitals)
            
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
        messages.error(request, 'Not Authorized')
        return render(request, 'patient-login.html') 
```

## View Multiple Hospital Information
![title](patient/Screenshot (254).png)
![title](patient/Screenshot (253).png)

## View hospital Doctor Information
```python
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
        messages.error(request, 'Not Authorized')
        return render(request, 'patient-login.html')   
```
## Doctor Information Page
![title](patient/Screenshot (213).png)

## View hospital Doctor Information
```python
 def booking(request, pk):
    patient = request.user.patient
    doctor = Doctor_Information.objects.get(doctor_id=pk)

    if request.method == 'POST':
        appointment = Appointment(patient=patient, doctor=doctor)
        date = request.POST['appoint_date']
        time = request.POST['appoint_time']
        appointment_type = request.POST['appointment_type']
        message = request.POST['message']

    
        transformed_date = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
        transformed_date = str(transformed_date)
         
        appointment.date = transformed_date
        appointment.time = time
        appointment.appointment_status = 'pending'
        appointment.serial_number = generate_random_string()
        appointment.appointment_type = appointment_type
        appointment.message = message
        appointment.save()
        
        if message:
            # Mailtrap
            patient_email = appointment.patient.email
            patient_name = appointment.patient.name
            patient_username = appointment.patient.username
            patient_phone_number = appointment.patient.phone_number
            doctor_name = appointment.doctor.name
        
            subject = "Appointment Request"
            
            values = {
                    "email":patient_email,
                    "name":patient_name,
                    "username":patient_username,
                    "phone_number":patient_phone_number,
                    "doctor_name":doctor_name,
                    "message":message,
                }
            
            html_message = render_to_string('appointment-request-mail.html', {'values': values})
            plain_message = strip_tags(html_message)
            
            try:
                send_mail(subject, plain_message, 'hospital_admin@gmail.com',  [patient_email], html_message=html_message, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
        
        
        messages.success(request, 'Appointment Booked')
        return redirect('patient-dashboard')

    context = {'patient': patient, 'doctor': doctor}
    return render(request, 'booking.html', context)
```
## Book Doctor Appointment Page
![title](patient/Screenshot (256).png)

## View Prescription Information
```python
 def prescription_view(request,pk):
      if request.user.is_patient:
        patient = Patient.objects.get(user=request.user)
        prescription = Prescription.objects.filter(prescription_id=pk)
        prescription_medicine = Prescription_medicine.objects.filter(prescription__in=prescription)
        prescription_test = Prescription_test.objects.filter(prescription__in=prescription)

        context = {'patient':patient,'prescription':prescription,'prescription_test':prescription_test,'prescription_medicine':prescription_medicine}
        return render(request, 'prescription-view.html',context)
      else:
         redirect('logout') 
```
## Prescription Page
![title](patient/Screenshot (212).png)

## View Test Payment Method
```python
def test_cart(request, pk):
    if request.user.is_authenticated and request.user.is_patient:
        # prescription = Prescription.objects.filter(prescription_id=pk)
        
        prescription = Prescription.objects.filter(prescription_id=pk)
        
        patient = Patient.objects.get(user=request.user)
        prescription_test = Prescription_test.objects.all()
        test_carts = testCart.objects.filter(user=request.user, purchased=False)
        test_orders = testOrder.objects.filter(user=request.user, ordered=False)
        
        if test_carts.exists() and test_orders.exists():
            test_order = test_orders[0]
            
            context = {'test_carts': test_carts,'test_order': test_order, 'patient': patient, 'prescription_test':prescription_test, 'prescription_id':pk}
            return render(request, 'test-cart.html', context)
        else:
            # messages.warning(request, "You don't have any test in your cart!")
            context = {'patient': patient,'prescription_test':prescription_test}
            return render(request, 'prescription-view.html', context)
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'patient-login.html') 
```
## Payment Page
![title](payment/Screenshot (249).png)


## View Report History
```python
def view_report(request,pk):
    if request.user.is_patient:
        patient = Patient.objects.get(user=request.user)
        report = Report.objects.filter(report_id=pk)
        specimen = Specimen.objects.filter(report__in=report)
        test = Test.objects.filter(report__in=report)

        # current_date = datetime.date.today()
        context = {'patient':patient,'report':report,'test':test,'specimen':specimen}
        return render(request, 'view-report.html',context)
    else:
        redirect('logout') 
```
## Report View
![title](payment/Screenshot (249).png)

## View Medical Shop
```python
  def pharmacy_shop(request):
    if request.user.is_authenticated and request.user.is_patient:
        
        patient = Patient.objects.get(user=request.user)
        medicines = Medicine.objects.all()
        orders = Order.objects.filter(user=request.user, ordered=False)
        carts = Cart.objects.filter(user=request.user, purchased=False)
        
        medicines, search_query = searchMedicines(request)
        
        if carts.exists() and orders.exists():
            order = orders[0]
            context = {'patient': patient, 'medicines': medicines,'carts': carts,'order': order, 'orders': orders, 'search_query': search_query}
            return render(request, 'Pharmacy/shop.html', context)
        else:
            context = {'patient': patient, 'medicines': medicines,'carts': carts,'orders': orders, 'search_query': search_query}
            return render(request, 'Pharmacy/shop.html', context)
    
    else:
        logout(request)
        messages.error(request, 'Not Authorized')
        return render(request, 'patient-login.html')  
```
## Medical Shop Page
![title](pharmacy/Screenshot (246).png)


## Medical Shop Cart
```python
def cart_view(request):
    if request.user.is_authenticated and request.user.is_patient:
         
        patient = Patient.objects.get(user=request.user)
        medicines = Medicine.objects.all()
        
        carts = Cart.objects.filter(user=request.user, purchased=False)
        orders = Order.objects.filter(user=request.user, ordered=False)
        if carts.exists() and orders.exists():
            order = orders[0]
            context = {'carts': carts,'order': order}
            return render(request, 'Pharmacy/cart.html', context)
        else:
            messages.warning(request, "You don't have any item in your cart!")
            context = {'patient': patient,'medicines': medicines}
            return render(request, 'pharmacy/shop.html', context)
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'patient-login.html') 

```
## Medical Shop cart page
![title](pharmacy/Screenshot (247).png)

