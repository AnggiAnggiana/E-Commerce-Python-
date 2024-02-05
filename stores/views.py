from django.shortcuts import render
from stores.models import Products

def homepage(request):
    smartphone = Products.objects.all()
    return render(request, 'stores/homepage.html', {
        'smartphone': smartphone,
    })