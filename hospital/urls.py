from django.urls import path
from . import views

# from . --> same directory
# Views functions and urls must be linked. # of views == # of urls
# App URL file - urls related to hospital


urlpatterns = [
    path('', views.hospital_home, name="hospital-url"),
]




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
