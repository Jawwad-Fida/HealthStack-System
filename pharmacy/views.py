import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from hospital.models import Patient
from pharmacy.models import Medicine


# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver


# Create your views here.

# function to return views for the urls

@login_required(login_url="login")
def pharmacy_single_product(request):
    return render(request, 'pharmacy/product-single.html')

@login_required(login_url="login")
def pharmacy_shop(request):
    if request.user.is_authenticated and request.user.is_patient:
         
        patient = Patient.objects.get(user=request.user)
        medicines = Medicine.objects.all()
        
        context = {'patient': patient, 'medicines': medicines}
        return render(request, 'pharmacy/shop.html', context)
    
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'patient-login.html')  
    
@login_required(login_url="login")
def demo_medicine_list(request):
    if request.user.is_authenticated and request.user.is_patient:
         
        patient = Patient.objects.get(user=request.user)
        medicines = Medicine.objects.all()
        
        context = {'patient': patient, 'medicines': medicines}
        return render(request, 'pharmacy/demo-medicine-list.html', context)
    
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'patient-login.html')  

@login_required(login_url="login")
def cart(request):
    return render(request, 'pharmacy/cart.html')

@login_required(login_url="login")
def checkout(request):
    return render(request, 'pharmacy/checkout.html')





# Create your views here.
