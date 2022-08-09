from django.contrib import admin

# Register your models here.
# # we are in same file path --> .models

from .models import Doctor_Information

admin.site.register(Doctor_Information)
