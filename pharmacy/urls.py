from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# from . --> same directory
# Views functions and urls must be linked. # of views == # of urls
# App URL file - urls related to hospital


urlpatterns = [
    # path('', views.hospital_home, name='hospital_home'),
    path('',views.pharmacy_homepage, name='pharmacy_homepage'),
    path('menu/', views.pharmacy_menu, name='pharmacy-menu'),
    path('single-product/', views.pharmacy_single_product, name='pharmacy-single-product'),
    path('shop/', views.pharmacy_shop, name='pharmacy-shop'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
