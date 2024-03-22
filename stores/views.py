from django.shortcuts import render, redirect, get_object_or_404
from stores.models import Profile, Products, Customers, Sellers, Smartphone, Foods, Comment_Smartphone, Comment_Foods, Shopping_Cart, ShippingType
import locale
from .forms import ProductForms, CustomersForms, SellerForms, SmartphoneForms, FoodForms, Comment_SmartphoneForm, Comment_FoodForm, ShippingTypeForm

from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

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
@login_required
def smartphone_show(request, smartphone_id):
    list_product_smartphone = get_object_or_404(Smartphone, pk=smartphone_id)
    review_smartphone = Comment_Smartphone.objects.filter(smartphone=list_product_smartphone)
    customerProfile = Customers.objects.get(owner_id=request.user.id)
    
    submitted = False
    if request.method == 'POST':
        # Check if the request method for adding product to the cart shop
        if 'add_to_cart' in request.POST:
            shopping_cart_item, created = Shopping_Cart.objects.get_or_create(
                user=customerProfile,
                product_smartphone=list_product_smartphone,
            )
            if created:
                messages.success(request, 'Product added to cart')
            else:
                messages.info(request, 'Product is already in the cart')
            return redirect('smartphone_show', smartphone_id=smartphone_id)
        
        # Check if the request method for submitting 'review comment' by user
        comment_smartphone_form = Comment_SmartphoneForm(request.POST, request.FILES, initial={'smartphone': list_product_smartphone, 'user': customerProfile})
        # picture_formset = CommentPictureFormSet(request.POST, request.FILES)
        if comment_smartphone_form.is_valid(): #and picture_formset.is_valid():
            comment_instance = comment_smartphone_form.save(commit=False)
            comment_instance.user = customerProfile
            comment_instance.smartphone = list_product_smartphone
            # comment_instance.pictures = comments
            print('comment_smartphone_form is okkay')
            comment_instance.save()
            
            messages.success(request, 'Review successfully added')
            return redirect(reverse('homepage') + '?submitted=True')
    else:
        comment_smartphone_form = Comment_SmartphoneForm(initial={'smartphone': list_product_smartphone, 'user': customerProfile})
        # picture_formset = CommentPictureFormSet()
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'stores/product_smartphone_list.html', {
        'submitted': submitted,
        'comment_smartphone_form': comment_smartphone_form,
        'list_product_smartphone': list_product_smartphone,
        'review_smartphone': review_smartphone,
        # 'picture_formset': picture_formset,
    })


# Show product (food) details in specific dynamic page
@login_required
def food_show(request, food_id):
    list_product_food = get_object_or_404(Foods, pk=food_id)
    review_food = Comment_Foods.objects.filter(food=list_product_food)
    customerProfile = Customers.objects.get(owner_id=request.user.id)
    
    submitted = False
    if request.method == 'POST':
        # Check if the request method for adding product to the cart shop
        if 'add_to_cart' in request.POST:
            shopping_cart_item, created = Shopping_Cart.objects.get_or_create(
                user=customerProfile,
                product_food=list_product_food,
            )
            if created:
                messages.success(request, 'Product added to cart')
            else:
                messages.info(request, 'Product is already in the cart')
            return redirect('food_show', food_id=food_id)
        
        # Check if the request method for submitting 'review comment' by user
        comment_food_form = Comment_FoodForm(request.POST, request.FILES, initial={'food': list_product_food, 'user': customerProfile})
        if comment_food_form.is_valid():
            comment_instance = comment_food_form.save(commit=False)
            comment_instance.user = customerProfile
            comment_instance.food = list_product_food
            comment_instance.save()
            
            messages.success(request, 'Review successfully added')
            return redirect(reverse('homepage') + '?submitted=True')
    else:
        comment_food_form = Comment_FoodForm(initial={'food': list_product_food, 'user': customerProfile})
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'stores/product_food_list.html', {
        'list_product_food': list_product_food,
        'review_food': review_food,
        'comment_food_form': comment_food_form,
        'submitted': submitted,
    })
    
# Show sellers store
@login_required
def seller_store(request, store_name):
    store_profile = get_object_or_404(Sellers, store_name=store_name)
    smartphone = Smartphone.objects.all()
    food = Foods.objects.all()
    
    return render(request, 'stores/store_profile.html', {
        'store_profile': store_profile,
        'smartphone': smartphone,
        'food': food,
    })

# Page to add new product
@login_required
def add_product(request):
    submitted = False
    product_add = ProductForms()
    if request.method == 'POST':
        if 'smartphone-form' in request.POST:
            smartphone_add = SmartphoneForms(request.POST, request.FILES)
            if smartphone_add.is_valid():
                smartphone_add.save()
                messages.success(request, 'Successfully added product')
                return redirect(reverse('homepage') + '?submitted=True')
        elif 'food-form' in request.POST:
            food_add = FoodForms(request.POST, request.FILES)
            if food_add.is_valid():
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


# Page to edit the product (smartphone)
@login_required
def edit_product_smartphone(request, smartphone_id):
    edit_product_smartphone = Smartphone.objects.get(pk=smartphone_id)
    edit_form = SmartphoneForms(request.POST or None, instance=edit_product_smartphone)
    if edit_form.is_valid():
        edit_form.save()
        messages.success(request, 'Successfully edit product details')
        return redirect('homepage')
    
    return render(request, 'stores/edit_product_smartphone.html', {
        'edit_product_smartphone': edit_product_smartphone,
        'edit_form': edit_form,
    })

# Page to edit the product (food)
@login_required
def edit_product_food(request, food_id):
    edit_product_food = Foods.objects.get(pk=food_id)
    edit_form = FoodForms(request.POST or None, instance=edit_product_food)
    if edit_form.is_valid():
        edit_form.save()
        messages.success(request, 'Successfully edit product details')
        return redirect('homepage')
    
    return render(request, 'stores/edit_product_food.html', {
        'edit_product_food': edit_product_food,
        'edit_form': edit_form,
    })


# to add Customers Profile
def add_customer_profile(request):
    submitted = False
    profile_instance = Profile.objects.get(user=request.user)
    print(f'1: {profile_instance}')
    if request.method == 'POST':
        profile_form = CustomersForms(request.POST, request.FILES, initial={'owner_id': profile_instance})
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile successfully completed')
            return redirect(reverse('homepage') + '?submitted=True')
    else:
        profile_form = CustomersForms(initial={'owner_id': profile_instance})
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'stores/add_customer_profile.html', {
        'submitted': submitted,
        'profile_form': profile_form,
    })

# To add Sellers Profile
@login_required
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


# Page of user profile
@login_required
def customerProfile(request):
    submitted = False
    customerProfile = Customers.objects.get(owner_id=request.user.id)
    print("customerProfile:", customerProfile)
    if request.method == 'POST':
        form = CustomersForms(request.POST or None, request.FILES or None, instance=customerProfile)
        if form.is_valid():
            edit_profile = form.save(commit=False)
            edit_profile.owner_id = request.user.id
            edit_profile.save()
            messages.success(request, 'Profile successfully edited')
            return redirect(reverse('homepage') + '?submitted=True')
    else:
        form = CustomersForms(instance=customerProfile)
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'stores/customerProfile.html', {
        'form': form,
        'submitted': submitted,
    })

# Search bar
@login_required
def search_results(request):
    if request.method == "POST":
        search = request.POST['search']
        smartphones = Smartphone.objects.filter(name__icontains=search)
        food = Foods.objects.filter(food_name__icontains=search)
        return render(request, 'stores/search_result.html', {
            'search': search,
            'smartphones': smartphones,
            'food': food,
        })
    else:
        return render(request, 'stores/search_result.html', {})
    
# Cart/Keranjang belanja
@login_required
def cart_shop(request):
    cart_date = Shopping_Cart.objects.all()
    profile_instance = Profile.objects.get(user=request.user)
    customer = Customers.objects.get(owner_id=profile_instance)
    # customer = Customers.objects.filter(owner_id=profile_instance)
    owner = Shopping_Cart.objects.filter(user=customer)
    # print(f'data semua: {cart_date}')
    # print(f'ownernya: {profile_instance}')
    # print(f'customer: {customer}')
    # print(f'user_saat ini: {owner}')
    
    if request.method == 'POST' and 'checkout' in request.POST:
        # Get the choosen product data
        selected_product_id = request.POST.getlist('selected_products')
        
        # Save product data into session
        request.session['selected_product_id'] = selected_product_id
        
        return redirect('checkout_product')
    
    return render(request, 'stores/cart_shop.html', {
        'cart_date': cart_date,
        'owner': owner,
    })
    
    
@login_required
def delete_cart_item(request, item_id):
    cart_item = Shopping_Cart.objects.get(pk=item_id)
    cart_item.delete()
    return redirect('cart_shop')

# Checkout product
@login_required
def checkout_product(request):
    selected_product_id = request.session.get('selected_product_id', [])
    # print(selected_product_id)
    print(f"Product Id di checkoutnya: {selected_product_id}")
    
    product_from_cart = Shopping_Cart.objects.filter(id__in=selected_product_id)
    
    shipping_types = ShippingType.objects.all()
    
    # form = ShippingTypeForm()
    
    if request.method == 'POST':
        form = ShippingTypeForm(request.POST)
        if form.is_valid():
            delivery_type = form.cleaned_data['delivery_type']
            price = ShippingType.objects.get(delivery_type=delivery_type).price
            form.instance = price
            form.save()
            return redirect('homepage')
    else:
        form = ShippingTypeForm()
    
    # Call calculate_estimated_time
    estimated_time_regular = calculate_estimated_time('Regular')
    estimated_time_fast = calculate_estimated_time('Fast')
    estimated_time_cargo = calculate_estimated_time('Cargo')
    
    return render (request, 'stores/checkout_product.html', {
        'product_from_cart': product_from_cart,
        'shipping_types': shipping_types,
        'form': form,
        'estimated_time_regular': estimated_time_regular,
        'estimated_time_fast': estimated_time_fast,
        'estimated_time_cargo': estimated_time_cargo,
    })

#Calculation for Shipping Options
def calculate_estimated_time(delivery_type):
    current_date = timezone.now()
    if delivery_type == 'Regular':
        estimated_time_start = current_date + timedelta(days=5)
        estimated_time_end = current_date + timedelta(days=7)
        estimated_time = f'{estimated_time_start.strftime("%d %B %Y")} - {estimated_time_end.strftime("%d %B %Y")}'
    elif delivery_type == 'Fast':
        estimated_time_start = current_date + timedelta(days=3)
        estimated_time_end = current_date + timedelta(days=5)
        estimated_time = f'{estimated_time_start.strftime("%d %B %Y")} - {estimated_time_end.strftime("%d %B %Y")}'
    elif delivery_type == 'Cargo':
        estimated_time_start = current_date + timedelta(days=6)
        estimated_time_end = current_date + timedelta(days=9)
        estimated_time = f'{estimated_time_start.strftime("%d %B %Y")} - {estimated_time_end.strftime("%d %B %Y")}'
    else:
        estimated_time = 'Delivery type is not recognized'
        
    return estimated_time