from django.db.models import Q
from .models import Medicine


def searchMedicines(request):
    
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
            
    medicines = Medicine.objects.filter(Q(name__icontains=search_query))
    
    return medicines, search_query
