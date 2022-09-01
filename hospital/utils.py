from django.db.models import Q
from .models import Patient, User
from doctor.models import Doctor_Information, Appointment


def searchDoctors(request):
    
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    #skills = Skill.objects.filter(name__icontains=search_query)
    
    doctors = Doctor_Information.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(hospital_name__name__icontains=search_query) |  
        Q(department__icontains=search_query))
    
    return doctors, search_query

# products = Products.objects.filter(price__range=[10, 100])
