from django.contrib import admin

# Register your models here.
# # we are in same file path --> .models

from .models import Hospital_Information, Patient, User, test_Cart, test_Order

admin.site.register(User)
admin.site.register(Hospital_Information)
admin.site.register(Patient)

# admin.site.register(Tag)
