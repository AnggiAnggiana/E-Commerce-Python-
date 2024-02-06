from django.shortcuts import render
from stores.models import Products, Sellers
import locale

def homepage(request):
    locale.setlocale(locale.LC_ALL, 'id_ID')
    
    smartphone = Products.objects.all()
    
    return render(request, 'stores/homepage.html', {
        'smartphone': smartphone,
    })