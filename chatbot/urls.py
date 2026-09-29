from django.urls import path 
from . import views 
  
  
urlpatterns = [ 
    path('', views.chatbot_view, name='chatbot'), 
] 