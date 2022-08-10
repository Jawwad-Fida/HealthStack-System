from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# from django.contrib.auth.models import User
from .models import Patient, User
from doctor.models import Doctor_Information


# # from django.core.mail import send_mail
# # from django.conf import settings


# error here --> two signals are working at the same time


# @receiver(post_save, sender=User)
# def createPatient(sender, instance, created, **kwargs):
#     if created:
#         Patient.objects.create(user=instance)


@receiver(post_save, sender=User)
def createPatient(sender, instance, created, **kwargs):
    if created:
        if instance.is_patient:
            user = instance
            Patient.objects.create(
                user=user, username=user.username, email=user.email)
        elif instance.is_doctor:
            user = instance
            Doctor_Information.objects.create(
                user=user, username=user.username, email=user.email)


@receiver(post_save, sender=Patient)
def updateUser(sender, instance, created, **kwargs):
    # user.profile or below (1-1 relationship goes both ways)
    patient = instance
    user = patient.user

    if created == False:
        user.first_name = patient.name
        user.username = patient.username
        user.email = patient.email
        user.save()


# @receiver(post_save, sender=User)
# def createDoctor(sender, instance, created, **kwargs):
#     if created:
#         Doctor_Information.objects.create(user=instance)
