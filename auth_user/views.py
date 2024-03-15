from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from stores.models import Profile
import random
import string
from django.core.mail import send_mail
import uuid
from decouple import config
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Successfully logged in"))
            return(redirect('homepage'))
        else:
            messages.error(request, ('Login Failed, username or password is wrong'))
            return(redirect('login_user'))
    else:
        return render(request, 'authentication/login_user.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Now you're logged out, please login back"))
    return(redirect('login_user'))

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)            
            user.is_active = False
            user.save()
            
            # Generate activation key
            activation_key = generate_activation_key()
            
            # Save activation key to user profile
            user.profile.activation_key = activation_key
            user.profile.save()
            
            # Generate activation token
            token = account_activation_token.make_token(user)
            
            subject = 'Here is your activation code'
            message = render_to_string('authentication/activation_email.html', {
                'user': user,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token,
                'activation_key': activation_key,
            })
            
            # Send email
            send_mail(subject, message, config('EMAIL_HOST_USER'), [user.email], fail_silently=False,)
            
            # Redirect to activation page
            # return redirect('activation_user')
            return redirect('activation_user', uidb64=urlsafe_base64_encode(force_bytes(user.pk)), token=token)
    else:
        form = RegisterForm()
        
    return render(request, 'authentication/register_user.html', {
        'form': form,
    })
    
def activation_user(request, uidb64, token):
    uid = urlsafe_base64_decode(uidb64).decode()
    user = User.objects.get(pk=uid)
    
    if request.method == 'POST':
        activation_key = request.POST.get('activation_key')
        if user.profile.activation_key == activation_key:
            user.is_active = True
            user.profile.activation_key = ''
            user.save()
            login(request, user)
            return redirect('add_customer_profile')
        else:
            messages.error(request, 'Invalid Activation Code')
            return render(request, 'authentication/activation_user.html', {})
    else:
        return render(request, 'authentication/activation_user.html', {})
    
def generate_activation_key():
    return ''.join(random.choices(string.digits, k=6))