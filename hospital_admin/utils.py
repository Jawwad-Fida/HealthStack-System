from django.db.models import Q
from pharmacy.models import Medicine


def searchMedicines(request):
    
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
            
    medicine = Medicine.objects.filter(Q(name__icontains=search_query))
    
    return medicine, search_query