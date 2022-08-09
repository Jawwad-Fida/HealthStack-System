from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# from . --> same directory
# Views functions and urls must be linked. # of views == # of urls
# App URL file - urls related to hospital


<<<<<<< HEAD
urlpatterns = [
    
=======
urlpatterns = [    
>>>>>>> 604656a23dc4c1b07dc1761e994638414054c65f
    path('', views.hospital_home,name='hospital_home'),
    # path('login/', views.signin,name='login'),
    path('doctor-dashboard/', views.doctor_dashboard,name='doctor_dashboard'),
    path('doctor-profile/', views.doctor_profile,name='doctor_profile'),
    path('doctor-change-password/', views.doctor_change_password,name='doctor_change_password'),
    path('change-password/', views.change_password,name='change_password'),
    path('search/', views.search,name='search'),
    path('doctor-register/', views.doctor_register,name='doctor_register'),
    path('doctor-profile-settings/', views.doctor_profile_settings,name='doctor_profile_settings'),
    path('my-patients/', views.my_patients,name='my_patients'),
    # path('login/', views.login_user),
    path('add-billing/', views.add_billing,name='add_billing'),
    path('add-prescription/', views.add_prescription,name='add_prescription'),
    path('appointments/', views.appointments,name='appointments'),
    path('booking-success/', views.booking_success,name='booking_success'),
    path('booking/', views.booking,name='booking'),
    path('edit-billing/', views.edit_billing,name='edit_billing'),
    path('edit-prescription/', views.edit_prescription,name='edit_prescription'),
    path('forgot-password/', views.forgot_password,name='forgot_password'),
    path('patient-dashboard/', views.patient_dashboard,name='patient_dashboard'),
    path('patient-profile/', views.patient_profile,name='patient_profile'),
    path('privacy-policy/', views.privacy_policy,name='privacy_policy'),
    path('profile-settings/', views.profile_settings,name='profile_settings'),
    path('register/', views.register,name='register'),
    path('schedule-timings/', views.schedule_timings,name='schedule_timings'),
    path('about-us/', views.about_us, name='about_us'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
