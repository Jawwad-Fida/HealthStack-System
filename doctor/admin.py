from django.contrib import admin

# Register your models here.
# # we are in same file path --> .models

from .models import Doctor_Information, Appointment, Report, Prescription, Education, Experience, Specimen, Test

admin.site.register(Doctor_Information)
admin.site.register(Appointment)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Report)
admin.site.register(Prescription)
admin.site.register(Test)
admin.site.register(Specimen)
