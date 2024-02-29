from django.shortcuts import render, redirect, get_object_or_404
from stores.models import Products, Customers, Sellers, Smartphone, Foods, Comment_Smartphone, Comment_Foods, Shopping_Cart
import locale
from .forms import ProductForms, ProfileForms, SellerForms, SmartphoneForms, FoodForms, Comment_SmartphoneForm, Comment_FoodForm #CommentPictureFormSet

from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse


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

# Search bar
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
def cart_shop(request):
    cart_data = Shopping_Cart.objects.all()
    
    return render(request, 'stores/cart_shop.html', {
        'cart_data': cart_data,
    })
    
def delete_cart_item(request, item_id):
    cart_item = Shopping_Cart.objects.get(pk=item_id)
    cart_item.delete()
    return redirect('cart_shop')