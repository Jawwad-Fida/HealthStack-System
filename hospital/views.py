from django.shortcuts import render, redirect
from django.http import HttpResponse


def hospital_home(request):
    return render(request, 'index.html')

# Create your views here.

# function to return views for the urls
