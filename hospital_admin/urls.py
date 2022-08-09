from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.admin_home, name='admin-home'),
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


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
