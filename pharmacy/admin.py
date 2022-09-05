from django.contrib import admin

# Register your models here.
from .models import Medicine, Pharmacist
admin.site.register(Medicine)
admin.site.register(Pharmacist)
