from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
<<<<<<< HEAD

# Create your views here.
=======
# Create your views here.

>>>>>>> main
def admin_home(request):
    return render(request, 'hospital_admin/index.html')