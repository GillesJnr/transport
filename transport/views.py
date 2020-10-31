from django.shortcuts import render, redirect
from .models import Users
from django.contrib.auth import (login as auth_login,  authenticate, logout as auth_logout)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, "transport/demo/layout.html")

def adduser(request):
    return render(request, "transport/demo/pages/ui-features/adduser.html")

def login(request):
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else: 
            # messages.info(request, 'Username or Password is incorrect. Try again')
            return redirect('login')
    else:  
        return render(request, 'transport\demo\pages\samples\login.html')

 
def logout(request):
    auth_logout(request)
    return redirect('login')


def view_customers(request):
    data = Users.objects.all().filter(user_type='C')
    return render(request, "transport/demo/pages/customers/index.html", {'data':data})