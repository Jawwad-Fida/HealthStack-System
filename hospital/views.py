from django.shortcuts import render, redirect
from django.http import HttpResponse

def hospital_home(request):
    return render(request, 'index.html')


