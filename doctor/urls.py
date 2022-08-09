from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


# from . --> same directory
# Views functions and urls must be linked. # of views == # of urls
# App URL file - urls related to hospital

urlpatterns = [
    path('', views.doctor_login, name='doctor-login'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor-dashboard'),
    path('doctor-profile/', views.doctor_profile, name='doctor-profile'),
    path('doctor-change-password/', views.doctor_change_password,
         name='doctor_change_password'),
    path('doctor-profile-settings/', views.doctor_profile_settings,
         name='doctor-profile-settings'),
    path('doctor-register/', views.doctor_register, name='doctor-register'),
    path('logout/', views.logoutUser, name='logout')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
