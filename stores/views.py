from django.shortcuts import render, redirect
from stores.models import Products
import locale
from .forms import Add_productForms

from django.contrib import messages
from django.urls import reverse

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

    
def add_product(request):
    submitted = False
    if request.method == 'POST':
        product_add = Add_productForms(request.POST, request.FILES)
        if product_add.is_valid():
            product_add.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('homepage') + '?submitted=True')
    else:
        product_add = Add_productForms()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'stores/product_add.html', {
        'product_add': product_add,
        'submitted': submitted,
    })