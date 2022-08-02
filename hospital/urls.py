from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# from . --> same directory
# Views functions and urls must be linked. # of views == # of urls
# App URL file - urls related to hospital


urlpatterns = [
    
    path('', views.hospital_home,name='hospital_home'),
    # path('login/', views.signin,name='login'),
    path('doctor-dashboard/', views.doctor_dashboard,name='doctor_dashboard'),
    path('doctor-profile/', views.doctor_profile,name='doctor_profile'),
    path('doctor-change-password/', views.doctor_change_password),
    path('change-password/', views.change_password),
    path('search/', views.search),
    path('doctor-register/', views.doctor_register),
    path('doctor-profile-settings/', views.doctor_profile_settings),
    path('my-patients/', views.my_patients),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = [

#     # make default homepage by using - path('')

#     path('', views.projects, name="projects"),

#     #path('projects/', views.return_projects, name='projects'),

#     # pass in a parameter to url
#     path('project/<str:pk>/', views.project, name="project"),

#     path('create-project/', views.createProject, name="create-project"),

#     path('update-project/<str:pk>/', views.updateProject, name="update-project"),

#     path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
# ]
