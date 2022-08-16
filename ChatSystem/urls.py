from django.urls import path
from . import views


urlpatterns = [
    path('chat/', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('messages/', views.message_list, name='message-list'),
    
    
]