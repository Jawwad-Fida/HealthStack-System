from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Patient


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
        user = instance
        Patient.objects.create(
            user=user, username=user.username, email=user.email)


# @receiver(post_save, sender=User)
# def createDoctor(sender, instance, created, **kwargs):
#     if created:
#         Doctor_Information.objects.create(user=instance)
