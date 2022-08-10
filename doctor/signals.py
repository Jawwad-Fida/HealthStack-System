from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# from django.contrib.auth.models import User

from .models import Doctor_Information
from hospital.models import User


# # from django.core.mail import send_mail
# # from django.conf import settings


@receiver(post_save, sender=Doctor_Information)
def updateUser(sender, instance, created, **kwargs):
    # user.profile or below (1-1 relationship goes both ways)
    doctor = instance
    user = doctor.user

    if created == False:
        user.first_name = doctor.name
        user.username = doctor.username
        user.email = doctor.email
        user.save()
