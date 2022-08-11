from django.db import models
import uuid

# import django user model
from django.contrib.auth.models import AbstractUser


# Create your models here.

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


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_hospital_admin = models.BooleanField(default=False)


class Hospital_Information(models.Model):
    # ('database value', 'display_name')
    HOSPITAL_TYPE = (
        ('private', 'Private hospital'),
        ('public', 'Public hospital'),
    )

    hospital_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    # hospital_image = models.ImageField(null=True, blank=True, default="default.jpg")

    featured_image = models.ImageField(
        upload_to='hospitals/', default='hospitals/default.png', null=True, blank=True)

    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    hospital_type = models.CharField(max_length=200, choices=HOSPITAL_TYPE)
    general_bed_no = models.IntegerField(null=True, blank=True)
    available_icu_no = models.IntegerField(null=True, blank=True)
    regular_cabin_no = models.IntegerField(null=True, blank=True)
    emergency_cabin_no = models.IntegerField(null=True, blank=True)
    vip_cabin_no = models.IntegerField(null=True, blank=True)

    # String representation of object
    def __str__(self):
        return str(self.name)


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='patient')
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    featured_image = models.ImageField(
        upload_to='patients/', default='patients/user-default.png', null=True, blank=True)

    blood_group = models.CharField(
        max_length=200, null=True, blank=True)
    # patient_allergy = models.TextField(null=True, blank=True)
    history = models.CharField(max_length=200, null=True, blank=True)

    dob = models.DateField(null=True, blank=True)
    nid = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


# class Payment_Details(models.Model):
#     payment_id = models.AutoField(primary_key=True, editable=False)
#     patient_name = models.CharField(max_length=200)
#     patient_email = models.CharField(max_length=200)
#     patient_phone_number = models.IntegerField(default=0)
#     paid_amount = models.IntegerField(default=0)
#     transaction_id = models.TextField(null=True, blank=True)
#     payment_date = models.DateField(null=True, blank=True)
#     status = models.CharField(max_length=200)
#     currency = models.CharField(max_length=200)
#     fee_type = models.CharField(max_length=200)

#     def __str__(self):
#         return self.patient_name


# class Admin_Information(models.Model):
#     ADMIN_TYPE = (
#         ('Hospital', 'Hospital Admin'),
#         ('Laboratory', 'Laboratory Admin'),
#         ('Pharmacy', 'Pharmacy Admin'),
#     )

#     admin_id = models.AutoField(primary_key=True, editable=False)
#     admin_username = models.CharField(max_length=200)
#     admin_phone_number = models.IntegerField(default=0)
#     admin_email = models.CharField(max_length=200, null=True, blank=True)
#     #admin_password = models.CharField(max_length=200, null=True, blank=True)
#     admin_role = models.CharField(
#         max_length=200, choices=ADMIN_TYPE, null=True, blank=True)

#     def __str__(self):
#         return self.admin_username


# class Report_Information(models.Model):

#     REPORT_TYPE = (
#         ('Urgent', 'Urgent'),
#         ('Normal', 'Normal'),
#     )

#     report_id = models.AutoField(primary_key=True, editable=False)
#     report_date = models.DateField(null=True, blank=True)
#     report_time = models.TimeField(null=True, blank=True)
#     report_type = models.CharField(
#         max_length=200, null=True, blank=True, choices=REPORT_TYPE)
#     delivery_date = models.TimeField(null=True, blank=True)
#     report_doctor = models.ForeignKey(
#         Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
#     patient_name = models.ForeignKey(
#         Patient, on_delete=models.CASCADE, null=True, blank=True)
#     Hospital_name = models.ForeignKey(
#         Hospital_Information, on_delete=models.CASCADE, null=True, blank=True)
#     report_description = models.TextField(null=True, blank=True)
#     report_image = models.ImageField(
#         null=True, blank=True, default="default.jpg")
#     total_report_fee = models.IntegerField(default=0)

#     def __str__(self):
#         return self.report_type


# class Test_information(models.Model):
#     test_id = models.AutoField(primary_key=True, editable=False)
#     test_name = models.CharField(max_length=200)
#     test_fee = models.IntegerField(default=0)
#     test_description = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.test_name
