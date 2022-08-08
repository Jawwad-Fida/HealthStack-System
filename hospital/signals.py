
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Doctor_Information, Patient

# from django.core.mail import send_mail
# from django.conf import settings

"""
This is not working at the moment. Probably needs a form and a view to work.
"""

# created --> check if user has been created the first time or not

# @receiver(post_save, sender=User)


# def createDoctor(sender, instance, created, **kwargs):
#     if created:
#         user = instance
#         Doctor_Information.objects.create(
#             user = user,
#             username = user.username,
#             email = user.email,
#             name = user.first_name,
#             )
        
def createPatient(sender, instance, created, **kwargs):
    if created:
        user = instance
        Patient.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
            )
        
def deletePatient(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

# When a user is created, a profile is immediately created
# sender is from User model (signal is sent from User model)
#post_save.connect(createDoctor, sender=User) # sender=User

post_save.connect(createPatient, sender=User) # sender=User

post_delete.connect(deletePatient, sender=Patient)