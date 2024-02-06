from django.shortcuts import render
from stores.models import Products
import locale

def homepage(request):
    locale.setlocale(locale.LC_ALL, 'id_ID')
    
    smartphone = Products.objects.all()
    
    return render(request, 'stores/homepage.html', {
        'smartphone': smartphone,
    })
    
def product_show(request, product_id):
    list_product = Products.objects.get(pk=product_id)
    
    return render(request, 'stores/product_list.html', {
        'list_product': list_product,
    })