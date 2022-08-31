from django.urls import path
from . import views


urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('<int:sender>/<int:receiver>/', views.message_view, name='chats'),
    path('chat/messages/', views.message_list, name='message-list'),
    path('chat/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    
    
    
]