# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin

# # from . --> same directory
# # Views functions and urls must be linked. # of views == # of urls
# # App URL file - urls related to hospital


# urlpatterns = [

#     path('', views.hospital_home, name='hospital_home'),
#     # path('login/', views.signin,name='login'),
#     path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
#     path('doctor-profile/', views.doctor_profile, name='doctor_profile'),
#     path('doctor-change-password/', views.doctor_change_password),
#     path('change-password/', views.change_password),
#     path('search/', views.search),
#     path('doctor-register/', views.doctor_register, name='doctor-register'),
#     path('doctor-profile-settings/', views.doctor_profile_settings),
#     path('my-patients/', views.my_patients),
#     # path('login/', views.login_user),
#     path('add-billing/', views.add_billing),
#     path('add-prescription/', views.add_prescription),
#     path('appointments/', views.appointments),
#     path('booking-success/', views.booking_success),
#     path('booking/', views.booking),
#     path('edit-billing/', views.edit_billing),
#     path('edit-prescription/', views.edit_prescription),
#     path('forgot-password/', views.forgot_password),
#     path('patient-dashboard/', views.patient_dashboard),
#     path('patient-profile/', views.patient_profile),
#     path('privacy-policy/', views.privacy_policy),
#     path('profile-settings/', views.profile_settings),
#     path('register/', views.registerPatient, name='patient-register'),
#     path('schedule-timings/', views.schedule_timings),


# ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
