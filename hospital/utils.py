from django.db.models import Q
from .models import Patient, User, Hospital_Information
from doctor.models import Doctor_Information, Appointment
from hospital_admin.models import hospital_department, specialization, service


def searchDoctors(request):
    
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    #skills = Skill.objects.filter(name__icontains=search_query)
    
    doctors = Doctor_Information.objects.filter(register_status='Accepted').distinct().filter(
        Q(name__icontains=search_query) |
        Q(hospital_name__name__icontains=search_query) |  
        Q(department__icontains=search_query))
    
    return doctors, search_query



def searchHospitals(request):
    
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    
    hospitals = Hospital_Information.objects.distinct().filter(Q(name__icontains=search_query))
    
    return hospitals, search_query


# def searchDepartmentDoctors(request, pk):
    
#     search_query = ''
    
#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')
        
    
#     departments = hospital_department.object.filter(hospital_department_id=pk).filter(
#         Q(doctor__name__icontains=search_query) |  
#         Q(doctor__department__icontains=search_query))
    
#     return departments, search_query

def searchDepartmentDoctors(request, pk):
    
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    departments = hospital_department.objects.get(hospital_department_id=pk)
    
    doctors = Doctor_Information.objects.filter(department_name=departments).filter(
        Q(name__icontains=search_query))
    
    # doctors = Doctor_Information.objects.filter(department_name=departments).filter(
    #     Q(name__icontains=search_query) |
    #     Q(specialization_name__name__icontains=search_query))
    
    return doctors, search_query



# products = Products.objects.filter(price__range=[10, 100])
