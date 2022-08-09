from django.db import models

import uuid

# import django user model
from django.contrib.auth.models import User
from hospital.models import Hospital_Information

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
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)

    degree = models.TextField(null=True, blank=True)
    department = models.CharField(
        max_length=200, choices=DOCTOR_TYPE, null=True, blank=True)

    featured_image = models.ImageField(
        upload_to='doctors/', default='doctors/user-default.png', null=True, blank=True)

    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    visiting_hour = models.TextField(null=True, blank=True)
    consultation_fee = models.IntegerField(null=True, blank=True)
    report_fee = models.IntegerField(null=True, blank=True)
    #doctor_password = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    # ForeignKey --> one to one relationship with Hospital_Information model.
    hospital_name = models.ForeignKey(
        Hospital_Information, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)
