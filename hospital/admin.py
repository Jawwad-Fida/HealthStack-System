from django.contrib import admin

# Register your models here.
# # we are in same file path --> .models

from .models import Hospital_Information, Doctor_Information

admin.site.register(Hospital_Information)
admin.site.register(Doctor_Information)

# admin.site.register(Tag)
