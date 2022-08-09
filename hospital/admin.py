from django.contrib import admin

# Register your models here.
# # we are in same file path --> .models

from .models import Hospital_Information, Patient

admin.site.register(Hospital_Information)
admin.site.register(Patient)

# admin.site.register(Tag)
