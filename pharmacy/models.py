from django.db import models
import uuid

from hospital.models import User, Patient

# Create your models here.

class Pharmacist(models.Model):
    pharmacist_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='pharmacist')
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    featured_image = models.ImageField(upload_to='doctors/', default='pharmacist/user-default.png', null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


class Medicine(models.Model):
    MEDICINE_TYPE = (
        ('tablets', 'tablets'),
        ('syrup', 'syrup'),
        ('powder', 'powder'),
        ('general', 'general'),
    )
    
    MEDICINE_CATEGORY = (
        ('nasal', 'nasal'),
        ('gastric', 'gastric'),
        ('skin', 'skin'),
        ('diarrhea', 'diarrhea'),
        ('infection', 'infection'),
        ('fever', 'fever'),
        ('cough', 'cough'),
        ('vitamins', 'vitamins'),
        ('oral cavity', 'oral cavity'),
        ('headache', 'headache'),
    )
    
    medicine_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    general_name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    featured_image = models.ImageField(upload_to='doctors/', default='medicines/default.png', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    medicine_type = models.CharField(max_length=200, choices=MEDICINE_TYPE, null=True, blank=True)
    medicine_category = models.CharField(max_length=200, choices=MEDICINE_CATEGORY, null=True, blank=True)
    price = models.CharField(max_length=200, choices=MEDICINE_TYPE, null=True, blank=True)
    # category
    serial_number = models.CharField(max_length=200, choices=MEDICINE_TYPE, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    


