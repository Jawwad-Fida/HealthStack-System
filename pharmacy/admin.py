from django.contrib import admin

# Register your models here.
from .models import Medicine, Pharmacist
from .models import Cart, Order

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Medicine)
admin.site.register(Pharmacist)
