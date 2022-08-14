"""healthstack URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hospital import views

# ROOT url file

# All urls paths of different pages will be in url patterns below

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login'),
    path('', include('hospital.urls')),
    path('doctor/', include('doctor.urls')),
    path('hospital_admin/', include('hospital_admin.urls')),
    path('sslcommerz/', include('sslcommerz.urls')),
    path('pharmacy/', include('pharmacy.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# path('login/', include('hospital.urls'),name='login'),
# path('doctor-dashboard/', include('hospital.urls')),

# path('doctor-profile/', include('hospital.urls')),

# path('doctor-change-password/', include('hospital.urls')),

# path('change-password/', include('hospital.urls')),

# path('search/', include('hospital.urls')),

# path('doctor-register/', include('hospital.urls')),

# path('doctor-profile-settings/', include('hospital.urls')),

# path('my-patients/', include('hospital.urls')),
