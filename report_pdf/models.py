from django.db import models

# Create your models here.
from hospital.models import Patient
from doctor.models import Doctor_Information


class Report_PDF(models.Model):

    report_pdf_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    specimen_id = models.CharField(max_length=200, null=True, blank=True)
    specimen_type = models.CharField(max_length=200, null=True, blank=True)
    collection_date = models.CharField(max_length=200, null=True, blank=True)
    receiving_date = models.CharField(max_length=200, null=True, blank=True)
    test_name = models.CharField(max_length=200, null=True, blank=True)
    result = models.CharField(max_length=200, null=True, blank=True)
    unit = models.CharField(max_length=200, null=True, blank=True)
    referred_value = models.CharField(max_length=200, null=True, blank=True)
    delivery_date = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.patient.username)