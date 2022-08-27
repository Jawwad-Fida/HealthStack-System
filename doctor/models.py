from django.db import models

import uuid

# import django user model
from hospital.models import Hospital_Information, User, Patient

# # Create your models here.

"""
null=True --> don't require a value when inserting into the database
blank=True --> allow blank value when submitting a form
auto_now_add --> automatically set the value to the current date and time
unique=True --> prevent duplicate values
primary_key=True --> set this field as the primary key
editable=False --> prevent the user from editing this field

django field types --> google it  # every field types has field options
Django automatically creates id field for each model class which will be a PK # primary_key=True --> if u want to set manual
"""
# Create your models here.


class Doctor_Information(models.Model):
    DOCTOR_TYPE = (
        ('Cardiologists', 'Cardiologists'),
        ('Neurologists', 'Neurologists'),
        ('Pediatricians', 'Pediatricians'),
        ('Physiatrists', 'Physiatrists'),
        ('Dermatologists', 'Dermatologists'),
    )
    doctor_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    department = models.CharField(
        max_length=200, choices=DOCTOR_TYPE, null=True, blank=True)

    featured_image = models.ImageField(
        upload_to='doctors/', default='doctors/user-default.png', null=True, blank=True)

    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    visiting_hour = models.CharField(max_length=200, null=True, blank=True)
    consultation_fee = models.IntegerField(null=True, blank=True)
    report_fee = models.IntegerField(null=True, blank=True)
    #doctor_password = models.CharField(max_length=200, null=True, blank=True)
    dob = models.CharField(max_length=200, null=True, blank=True)
    
    # Education
    institute = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    completion_year = models.CharField(max_length=200, null=True, blank=True)
    
    # degree
    
    # work experience
    work_place = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    start_year = models.CharField(max_length=200, null=True, blank=True)
    end_year = models.CharField(max_length=200, null=True, blank=True)
    
    

    # ForeignKey --> one to one relationship with Hospital_Information model.
    hospital_name = models.ForeignKey(
        Hospital_Information, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


"""
 amount, followup, status


appointment_type,payment_status  # appointment_status --> pending, confirmed, cancelled

"""


class Appointment(models.Model):
    # ('database value', 'display_name')
    APPOINTMENT_TYPE = (
        ('report', 'report'),
        ('checkup', 'checkup'),
    )
    APPOINTMENT_STATUS = (
        ('pending', 'pending'),
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled'),
    )

    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    doctor = models.ForeignKey(
        Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True)
    appointment_type = models.CharField(
        max_length=200, choices=APPOINTMENT_TYPE)
    appointment_status = models.CharField(
        max_length=200, choices=APPOINTMENT_STATUS)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    payment_status = models.CharField(
        max_length=200, null=True, blank=True, default='pending')
    transaction_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.patient.username)


class Report(models.Model):

    report_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    test_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    result = models.CharField(max_length=200, null=True, blank=True)
    delivery_date = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.patient.username)
        
class Prescription(models.Model):

    # medicine name, quantity, days, time, description, test, test_descrip
    prescription_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    
    medicine_name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.CharField(max_length=200, null=True, blank=True)
    days = models.CharField(max_length=200, null=True, blank=True)
    time = models.CharField(max_length=200, null=True, blank=True)
    medicine_description = models.TextField(null=True, blank=True)

    test_name = models.CharField(max_length=200, null=True, blank=True)
    test_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.doctor.username)
