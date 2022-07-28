from django.contrib import admin

# Register your models here.
# # we are in same file path --> .models

from .models import Hospital_Information, Doctor_Information, Admin_Information, Patient, Appointment, Payment_Details, Report_Information, Test_information

admin.site.register(Hospital_Information)
admin.site.register(Doctor_Information)
admin.site.register(Admin_Information)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Payment_Details, verbose_name="Payment_Details")
admin.site.register(Report_Information)
admin.site.register(Test_information)

# admin.site.register(Tag)
