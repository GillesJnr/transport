from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import (login as auth_login,  authenticate, logout as auth_logout)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date


# Create your views here.

@login_required(login_url='login')
def home(request):
    today = date.today()
    # income = Income.objects.all().filter(date__year=today.year).aggregate(sum('amount'))
    # context = {
    #     'income' : income,
    # }
    return render(request, "transport/demo/layout.html")

@login_required(login_url='login')
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


@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def view_customers(request):
    data = Users.objects.all().filter(user_type='C')
    return render(request, "transport/demo/pages/customers/index.html", {'data':data})


@login_required(login_url='login')
def view_users(request):
    data = Users.objects.all().filter(Q(user_type='S') | Q(user_type='O'))
    return render(request, "transport/demo/pages/customers/index.html", {'data':data})


@login_required(login_url='login')
def view_drivers(request):
    data = Users.objects.all().filter(user_type='D')
    return render(request, "transport/demo/pages/customers/index.html", {'data':data})