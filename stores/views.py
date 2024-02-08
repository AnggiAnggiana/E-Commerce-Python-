from django.shortcuts import render, redirect, get_object_or_404
from stores.models import Products, Customers
import locale
from .forms import ProductForms, ProfileForms

from django.contrib import messages
from django.urls import reverse


def homepage(request):
    locale.setlocale(locale.LC_ALL, 'id_ID')
    
    smartphone = Products.objects.all()
    
    return render(request, 'stores/homepage.html', {
        'smartphone': smartphone,
    })
    
# Show product details in specific dynamic page
def product_show(request, product_id):
    list_product = Products.objects.get(pk=product_id)
    
    return render(request, 'stores/product_list.html', {
        'list_product': list_product,
    })

# Page to add new product
def add_product(request):
    submitted = False
    if request.method == 'POST':
        product_add = ProductForms(request.POST, request.FILES)
        if product_add.is_valid():
            product_add.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('homepage') + '?submitted=True')
    else:
        product_add = ProductForms()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'stores/product_add.html', {
        'product_add': product_add,
        'submitted': submitted,
    })
    
# to add Customers profile
def user_profile(request):
    submitted = False
    if request.method == 'POST':
        profile_form = ProfileForms(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile successfully edited')
            return redirect(reverse('user_profile') + '?submitted=True')
    else:
        profile_form = ProfileForms()
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'stores/user_profile.html', {
        'submitted': submitted,
        'profile_form': profile_form,
    })
    
# Page to edit the product
def edit_product(request, product_id):
    edit_product = Products.objects.get(pk=product_id)
    edit_form = ProductForms(request.POST or None, instance=edit_product)
    if edit_form.is_valid():
        edit_form.save()
        messages.success(request, 'Successfully edit product details')
        return redirect('homepage')
    
    return render(request, 'stores/edit_product.html', {
        'edit_product': edit_product,
        'edit_form': edit_form,
    })
    
    
# Page of user profile
# def user_profile(request):
#     submitted = False
#     user_profile = Customers.objects.filter(owner_id=request.user.id)
#     if request.method == 'POST':
#         profile_form = ProfileForms(request.POST or None, request.FILES or None, instance=user_profile)
#         if profile_form.is_valid():
#             edit_profile = profile_form.save(commit=False)
#             edit_profile.owner_id = request.user.id
#             edit_profile.save()
#             messages.success(request, 'Profile successfully edited')
#             return redirect(reverse('user_profile') + '?submitted=True')
#     else:
#         profile_form = ProfileForms()
#         if 'submitted' in request.GET:
#             submitted = True
            
#     return render(request, 'stores/user_profile.html', {
#         'submitted': submitted,
#         'profile_form': profile_form,
#         'user_profile': user_profile,
#     })