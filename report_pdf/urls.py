from unicodedata import name
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('', views.report_home, name='report_home'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
