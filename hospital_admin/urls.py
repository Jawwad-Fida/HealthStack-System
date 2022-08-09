from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('',views.admin_home,name='admin_home'),
    # path('appointment-list'),
    
    path('doctor-list/', views.doctor_list,name='doctor_list'),
    
    path('forgot-password/', views.admin_forgot_password,name='admin_forgot_password'),
    
    
   
    # path('invoice/', ),
    # path('invoice-report/', ),
    # path('lock-screen/', ),
    path('login/',views.admin_login,name='admin_login'),
    # path('patient-list/', ),
   
    path('profile/', views.admin_profile,name='admin_profile'),
    path('register/', views.admin_register,name='admin_register')
    
    # path('specialitites',),
   
    # path('transactions-list/', ),
]







urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)