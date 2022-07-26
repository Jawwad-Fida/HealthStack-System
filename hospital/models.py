from django.db import models
import uuid

# Create your models here.

# django automatically creates an id field for each model (int)
# null=True --> don't require a value when inserting into the database
# blank=True --> allow blank value when submitting a form
# auto_now_add --> automatically set the value to the current date and time
# unique=True --> prevent duplicate values
# primary_key=True --> set this field as the primary key
# editable=False --> prevent the user from editing this field

# django field types --> google it  # every field types has field options
# Django automatically creates id field for each model class which will be a PK # primary_key=True --> if u want to set manual


# hospital_id int

class Hospital_Information(models.Model):
    # ('database value', 'display_name')
    HOSPITAL_TYPE = (
        ('private', 'Private hospital'),
        ('public', 'Public hospital'),
    )

    hospital_id = models.AutoField(primary_key=True, editable=False)
    # override default id field. UUIDField is a special field to store universally unique identifiers.
    hospital_name = models.CharField(max_length=200)
    hospital_address = models.TextField(null=True, blank=True)
    hospital_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    hospital_email = models.CharField(max_length=200, null=True, blank=True)
    hospital_phone_number = models.IntegerField(default=0)
    hospital_type = models.CharField(max_length=200, choices=HOSPITAL_TYPE)
    emergency_cabin_no = models.IntegerField(default=0)
    regular_cabin_no = models.IntegerField(default=0)
    available_icu_no = models.IntegerField(default=0)
    general_bed_no = models.IntegerField(default=0)
    vip_cabin_no = models.IntegerField(default=0)

    # String representation of object

    def __str__(self):
        return self.hospital_name


class Doctor_Information(models.Model):
    DOCTOR_TYPE = (
        ('Cardiologists', 'Cardiologists'),
        ('Neurologists', 'Neurologists'),
        ('Pediatricians', 'Pediatricians'),
        ('Physiatrists', 'Physiatrists'),
        ('Dermatologists', 'Dermatologists'),
    )
    doctor_id = models.AutoField(primary_key=True, editable=False)
    doctor_name = models.CharField(max_length=200)

    doctor_degree = models.TextField()
    doctor_department = models.CharField(
        max_length=200, choices=DOCTOR_TYPE, null=True, blank=True)
    doctor_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    doctor_email = models.CharField(max_length=200)
    doctor_phone_number = models.IntegerField(default=0)
    doctor_visiting_hour = models.TextField(null=True, blank=True)
    doctor_consultation_fee = models.IntegerField(default=0)
    doctor_report_fee = models.IntegerField(default=0)

    # ForeignKey --> one to one relationship with Hospital_Information model.
    Hospital_Name = models.ForeignKey(
        Hospital_Information, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.doctor_name
