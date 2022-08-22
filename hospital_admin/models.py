from django.db import models
from hospital.models import User, Hospital_Information
from doctor.models import Doctor_Information


# Create your models here.

class Admin_Information(models.Model):
    ADMIN_TYPE = (
        ('hospital', 'hospital'),
        ('laboratory', 'laboratory'),
        ('pharmacy', 'pharmacy'),
    )

    admin_id = models.AutoField(primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='hospital_admin')
    username = models.CharField(null=True, blank=True, max_length=200)
    name = models.CharField(max_length=200, null=True, blank=True)
    featured_image = models.ImageField(
        upload_to='admin/', default='admin/user-default.png', null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(
        max_length=200, choices=ADMIN_TYPE, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


class Clinical_Laboratory_Technician(models.Model):
    technician_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='technician')
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    featured_image = models.ImageField(upload_to='technician/', default='technician/user-default.png', null=True, blank=True)

    def __str__(self):
        return str(self.user.username)
    

# class department(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True)
#     # username = models.CharField(max_length=200, null=True, blank=True)
#     # age = models.IntegerField(null=True, blank=True)
#     # email = models.EmailField(max_length=200, null=True, blank=True)
#     # phone_number = models.IntegerField(null=True, blank=True)
#     # featured_image = models.ImageField(upload_to='technician/', default='technician/user-default.png', null=True, blank=True)

#     def __str__(self):
#         return str(self.name)