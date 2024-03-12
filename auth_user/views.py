from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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