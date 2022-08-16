import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver


# Create your views here.

# function to return views for the urls


def pharmacy_homepage(request):
    return render(request, 'pharmacy/index.html')

def pharmacy_menu(request):
    return render(request, 'pharmacy/menu.html')

def pharmacy_single_product(request):
    return render(request, 'pharmacy/product-single.html')

def pharmacy_shop(request):
    return render(request, 'pharmacy/shop.html')

def cart(request):
    return render(request, 'pharmacy/cart.html')

def checkout(request):
    return render(request, 'pharmacy/checkout.html')

def cart(request):
    return render(request, 'pharmacy/cart.html')




# Create your views here.
