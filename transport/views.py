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
    return render(request, "transport/demo/pages/users/index.html", {'data':data})


@login_required(login_url='login')
def view_drivers(request):
    data = Users.objects.all().filter(user_type='D')
    return render(request, "transport/demo/pages/drivers/index.html", {'data':data})

@login_required(login_url='login')
def manage_vehicles(request):
    data = Vehicles.objects.all()
    return render(request, "transport/demo/pages/vehicles/index.html", {'data':data})

@login_required(login_url='login')
def vehicles_group(request):
    data = VehicleGroup.objects.all()
    vehicle_data = Vehicles.objects.all()
    context = {
        'data': data,
        'vehicle_data': vechicle_data,
    }
    return render(request, "transport/demo/pages/vehicles/vehiclesgroup.html", context)

@login_required(login_url='login')
def manage_income(request):
    pass

@login_required(login_url='login')
def manage_expense(request):
    pass

@login_required(login_url='login')
def new_booking(request):
    pass

@login_required(login_url='login')
def manage_booking(request):
    pass

@login_required(login_url='login')
def booking_calendar(request):
    pass


@login_required(login_url='login')
def delinquent_report(request):
    pass

@login_required(login_url='login')
def monthly_report(request):
    pass

@login_required(login_url='login')
def booking_report(request):
    pass

@login_required(login_url='login')
def users_report(request):
    pass


@login_required(login_url='login')
def fuel_report(request):
    pass

@login_required(login_url='login')
def driver_report(request):
    pass

@login_required(login_url='login')
def customer_report(request):
    pass


@login_required(login_url='login')
def vendor_report(request):
    pass


@login_required(login_url='login')
def yearly_report(request):
    pass

@login_required(login_url='login')
def add_fuel(request):
    pass


@login_required(login_url='login')
def fuel_history(request):
    pass

@login_required(login_url='login')
def add_vendor(request):
    pass


@login_required(login_url='login')
def manage_vendor(request):
    pass


@login_required(login_url='login')
def add_workorder(request):
    pass

@login_required(login_url='login')
def add_note(request):
    pass

@login_required(login_url='login')
def manage_note(request):
    pass

@login_required(login_url='login')
def add_reminder(request):
    pass


@login_required(login_url='login')
def manage_reminder(request):
    pass

@login_required(login_url='login')
def service_item(request):
    pass

@login_required(login_url='login')
def general_settings(request):
    pass

@login_required(login_url='login')
def api_settings(request):
    pass

@login_required(login_url='login')
def cancellation_reason(request):
    pass

@login_required(login_url='login')
def email_notification(request):
    pass

@login_required(login_url='login')
def email_content(request):
    pass

@login_required(login_url='login')
def fare_settings(request):
    pass

@login_required(login_url='login')
def expense_categories(request):
    pass

@login_required(login_url='login')
def income_categories(request):
    pass

