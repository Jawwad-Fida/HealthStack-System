from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.admin_home, name='admin-home'),
    path('appointment_list/', views.appointment_list, name='appointment-list'),
    path('doctor-list/', views.doctor_list, name='doctor_list'),
    path('forgot-password/', views.admin_forgot_password,
         name='admin_forgot_password'),
    path('hospital-list/', views.hospital_list, name='hospital-list'),
    path('add-hospital/', views.add_hospital, name='add-hospital'),
    path('edit-hospital/', views.edit_hospital, name='edit-hospital'),
    path('add-hospital/', views.add_hospital, name='add-hospital'),
    path('edit-hospital/', views.edit_hospital, name='edit-hospital'),
    path('invoice/', views.invoice, name='invoice'),
    path('invoice-report/', views.invoice_report, name='invoice_report'),
    path('lock-screen/', views.lock_screen, name='lock_screen'),
    path('login/', views.admin_login, name='admin_login'),
    path('patient-list/', views.patient_list, name='patient_list'),
    path('profile/', views.admin_profile, name='admin_profile'),

    path('register/', views.admin_register, name='admin_register'),

    path('transactions-list/', views.transactions_list, name='transactions_list'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
