from django.contrib import admin

# Register your models here.
from .models import Admin_Information, Clinical_Laboratory_Technician, hospital_department, specialization, service ,Test_Information

admin.site.register(Admin_Information)

admin.site.register(Clinical_Laboratory_Technician)

admin.site.register(hospital_department)

admin.site.register(specialization)

admin.site.register(service)

admin.site.register(Test_Information)
