from django.contrib import admin

# Register your models here.
# # we are in same file path --> .models

from .models import Doctor_Information, Appointment, Report, Prescription, Education, Experience, Specimen, Test,Prescription_medicine,Prescription_test,testCart,testOrder, Doctor_review


admin.site.register(Doctor_Information)
admin.site.register(Appointment)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Report)
admin.site.register(Prescription)
admin.site.register(Test)
admin.site.register(Specimen)
admin.site.register(Prescription_medicine)
admin.site.register(Prescription_test)
admin.site.register(testCart)
admin.site.register(testOrder)
admin.site.register(Doctor_review)
