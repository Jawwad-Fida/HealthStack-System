from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from django.contrib import admin
=======
>>>>>>> main


urlpatterns = [
    
<<<<<<< HEAD
    # path('', views.hospital_home,name='hospital_home'),
    # path('login/', views.signin,name='login'),
    path('', views.admin_home,name='admin_home')
    # path('doctor-profile/', views.doctor_profile,name='doctor_profile'),
    # path('doctor-change-password/', views.doctor_change_password),
    # path('change-password/', views.change_password),
    # path('search/', views.search),
    # path('doctor-register/', views.doctor_register),
    # path('doctor-profile-settings/', views.doctor_profile_settings),
    # path('my-patients/', views.my_patients),
    #path('login/', views.login),
    
]

=======
    path('',views.admin_home,name='admin_home'),
    # path('appointment-list'),
    # path('components/', ),
    # path('data-tables/',),
    # path('doctor-list/', ),
    # path('error-404/', ),
    # path('error-500/', ),
    # path('forgot-password/', ),
    # path('form-basic-input/', ),
    
    # path('form-horizontal/', ),
    # path('form-input-groups/', ),
    # path('form-masks/', ),
    # path('form-validation/', ),
    # path('form-vertical/', ),
    # path('invoice/', ),
    # path('invoice-report/', ),
    # path('lock-screen/', ),
    # path('login/', ),
    # path('patient-list/', ),
    # path('reviews/', ),
    # path('profile/', ),
    # path('register/', ),
    # path('settings/', ),
    # path('specialitites',),
    # path('table-basic/', ),
    # path('transactions-list/', ),
]







>>>>>>> main
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)