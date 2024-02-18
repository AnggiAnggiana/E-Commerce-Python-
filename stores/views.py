from django.shortcuts import render, redirect, get_object_or_404
from stores.models import Products, Customers, Smartphone, Foods
import locale
from .forms import ProductForms, ProfileForms, SellerForms, SmartphoneForms, FoodForms

from django.contrib import messages
from django.urls import reverse


def homepage(request):
    locale.setlocale(locale.LC_ALL, 'id_ID')
    
    product = Products.objects.all()
    smartphone = Smartphone.objects.all()
    food = Foods.objects.all()
    
    return render(request, 'stores/homepage.html', {
        'product': product,
        'smartphone': smartphone,
        'food': food,
    })
    
# Show product (smartphone) details in specific dynamic page
def smartphone_show(request, smartphone_id):
    list_product_smartphone = Smartphone.objects.get(pk=smartphone_id)
    
    return render(request, 'stores/product_list.html', {
        'list_product_smartphone': list_product_smartphone,
    })

# Page to add new product
def add_product(request):
    submitted = False
    product_add = ProductForms()
    if request.method == 'POST':
        smartphone_add = SmartphoneForms(request.POST, request.FILES)
        food_add = FoodForms(request.POST, request.FILES)
        if smartphone_add.is_valid():
            smartphone_add.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('homepage') + '?submitted=True')
        elif food_add.is_valid():
            food_add.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('homepage') + '?submitted=True')
    else:
        smartphone_add = SmartphoneForms()
        food_add = FoodForms()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'stores/product_add.html', {
        'product_add': product_add,
        'smartphone_add': smartphone_add,
        'food_add': food_add,
        'submitted': submitted,
    })
    
# to add Customers Profile
def add_customer_profile(request):
    submitted = False
    if request.method == 'POST':
        profile_form = ProfileForms(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile successfully completed')
            return redirect(reverse('homepage') + '?submitted=True')
    else:
        profile_form = ProfileForms()
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'stores/add_customer_profile.html', {
        'submitted': submitted,
        'profile_form': profile_form,
    })
    
# To add Sellers Profile
def add_seller_profile(request):
    submitted = False
    if request.method == 'POST':
        profile_form = SellerForms(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your Seller Profile Successfully completed')
            return redirect(reverse('homepage') + '?submitted=True')
    else:
        profile_form = SellerForms()
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'stores/add_seller_profile.html', {
        'submitted': submitted,
        'profile_form': profile_form,
    })
    
# Page to edit the product
def edit_product_smartphone(request, smartphone_id):
    edit_product_smartphone = Smartphone.objects.get(pk=smartphone_id)
    edit_form = SmartphoneForms(request.POST or None, instance=edit_product_smartphone)
    if edit_form.is_valid():
        edit_form.save()
        messages.success(request, 'Successfully edit product details')
        return redirect('homepage')
    
    return render(request, 'stores/edit_product.html', {
        'edit_product': edit_product_smartphone,
        'edit_form': edit_form,
    })
    
    
# Page of user profile
def customerProfile(request):
    submitted = False
    customerProfile = Customers.objects.get(owner_id=request.user.id)
    if request.method == 'POST':
        form = ProfileForms(request.POST or None, request.FILES or None, instance=customerProfile)
        if form.is_valid():
            edit_profile = form.save(commit=False)
            edit_profile.owner_id = request.user.id
            edit_profile.save()
            messages.success(request, 'Profile successfully edited')
            return redirect(reverse('homepage') + '?submitted=True')
    
    else:
        form = ProfileForms(instance=customerProfile)
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'stores/customerProfile.html', {
        'form': form,
        'submitted': submitted,
    })