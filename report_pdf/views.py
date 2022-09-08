from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.db.models import Q, Count
import random
import string
from datetime import datetime, timedelta
import datetime
import re


from hospital.models import Patient
from doctor.models import Doctor_Information, Report
from .models import Report_PDF


# Create your views here.

def report_home(request):
    return render(request, 'main_report.html')