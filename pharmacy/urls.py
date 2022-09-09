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
    path('single-product/', views.pharmacy_single_product, name='pharmacy-single-product'),
    path('shop/', views.pharmacy_shop, name='pharmacy_shop'),
    path('cart/', views.cart_view, name='cart'),
    path('remove-item/<int:pk>/', views.remove_from_cart, name='remove-item'),
    path('checkout/', views.checkout, name='checkout'),
    path('demo-medicine-list/', views.demo_medicine_list, name='demo-medicine-list'),
    path('shop/<int:pk>', views.add_to_cart, name='shop'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
