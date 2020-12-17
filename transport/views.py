from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import (login as auth_login,  authenticate, logout as auth_logout)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date, timedelta
from django.db.models import Count, Sum, Avg
from .forms import *


# Create your views here.

def nat(request):
    return render(request, 'transport/demo/pages/ui-features/adduser.html')

@login_required(login_url='login')
def home(request):
    # today = date.today()
    # income = Income.objects.all().filter(date__year=today.year).aggregate(sum('amount'))
    income = Income.objects.values('amount').aggregate(Sum('amount')).get('amount__sum')
    income = "{:.2f}".format(income)

    expense = Expense.objects.values('amount').aggregate(Sum('amount')).get('amount__sum')
    expense = "{:.2f}".format(expense)

    avg_income = Income.objects.values('amount').aggregate(Avg('amount')).get('amount__avg')
    avg_income = "{:.2f}".format(avg_income)

    users = Users.objects.all().aggregate(Count('name')).get('name__count')
    drivers = Users.objects.all().filter(user_type='D').aggregate(Count('name')).get('name__count')
    customers = Users.objects.all().filter(user_type='C').aggregate(Count('name')).get('name__count')

    vendors = Vendors.objects.all().aggregate(Count('name')).get('name__count')
    bookings = Bookings.objects.all().aggregate(Count('id')).get('id__count')
    vehicles = Vehicles.objects.all().aggregate(Count('make')).get('make__count')


    context = {
        'income' : income,
        'expense' : expense,
        'avg_income' : avg_income,
        'users' : users, 
        'drivers' : drivers,
        'customers' : customers, 
        'vendors' : vendors, 
        'bookings' : bookings,
        'vehicles' : vehicles,
    }
    return render(request, "transport/demo/layout.html", context)

@login_required(login_url='login')
def adduser(request):
    if request.method == 'POST':
        form1 = AddUserForm(request.POST)
        form2 = AddUsersForm(request.POST , request.FILES)
        
        if form2.is_valid():
            instance = form2.save(commit=False)
            instance.user_type = 'O'
            instance.save()
        else:
            print(form2.errors)
        if form1.is_valid():
            instance1 = form1.save(commit=False)
            instance1.username = form2.email
            instance1.first_name = form2.name.split(" ")[0]
            instance1.last_name = form2.name.split(" ")[1:]
            instance1.email = form2.email
            instance1.is_staff = True
            instance1.save()
        else:
            print(form1.errors)
        return render(request, "transport/demo/pages/users/index.html")
    else:
        form1 = AddUserForm()
        form2 = AddUsersForm()
        context = {
            'form1' : form1,
            'form2' : form2,
        }
        return render(request, "transport/demo/pages/users/create-user.html", context)
    return render(request, "home")

def login(request):
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            message = "Incorrect Username or Password"
            return render(request, 'transport\demo\pages\samples\login.html', {
                'message': message, 
                })            
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
def add_vehicle(request):
    if request.method == "GET": 
        form = VehicleForm()
        return render(request, 'transport/demo/pages/vehicles/create-vehicle.html', {'form': form})
    else:
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_vehicles')
        else:
            print( form.errors )
            return render(request, 'transport/demo/pages/vehicles/create-vehicle.html', {'form': form})
            

@login_required(login_url='login')
def edit_vehicle(request, id):
    if request.method == "GET":
        vehicle = Vehicles.objects.get(pk=id)
        form = VehicleForm(instance=vehicle)
        return render(request, 'transport/demo/pages/vehicles/create-vehicle.html', {'form': form})
    else:
        vehicle = Vehicles.objects.get(pk=id)
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('manage_vehicles')
        else:
            return render(request, 'transport/demo/pages/vehicles/create-vehicle.html', {'form': form})


@login_required(login_url='login')
def delete_vehicle(request, id):
    vehicle = Vehicles.objects.get(pk=id)
    vehicle.delete()
    return redirect('manage_vehicles')



@login_required(login_url='login')
def vehicles_group(request):
    data = VehicleGroup.objects.all()
    vehicle_data = Vehicles.objects.all()
    group_total = Vehicles.objects.aggregate(Count('group'))['group__count']
    user_total = Vehicles.objects.aggregate(Count('vehicles_user'))['vehicles_user__count']
    context = {
        'data': data,
        'vehicle_data': vehicle_data,
        'group_total':  group_total,
        'user_total': user_total,
    }
    return render(request, "transport/demo/pages/vehicles/vehiclesgroup.html", context)


@login_required(login_url="login")
def add_vehicle_group(request):
    if request.method == "GET":
        form = VehicleGroupForm()
        return render(request, "transport/demo/pages/vehicles/create-vehicle-group.html", {'form': form})
    else:
        form = VehicleGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicles_group')
        else:
            return render(request, 'transport/demo/pages/vehicles/create-vehicle-group.html', {'form': form})


@login_required(login_url='login')
def update_vehicle_group(request, id):
    vehicle_group = VehicleGroup.objects.get(pk=id)
    if request.method == 'GET':
        form = VehicleGroupForm(instance=vehicle_group)
        return render(request, 'transport/demo/pages/vehicles/create-vehicle-group.html', {'form': form})
    else:
        form = VehicleGroupForm(request.POST, instance=vehicle_group)
        if form.is_valid():
            form.save()
            return redirect('vehicles_group')
        else:
            return render(request, 'transport/demo/pages/vehicles/vehiclegroup.html', {'form': form})


@login_required(login_url='login')
def delete_vehicle_group(request, id):
    vehicle_group = VehicleGroup.objects.get(pk=id)
    vehicle_group.delete()
    return redirect('vehicles_group')


@login_required(login_url='login')
def manage_income(request):
    form = IncomeForm()
    data = Income.objects.all()
    context = {
        'form': form,
        'data': data,
    }
    return render(request, 'transport/demo/pages/transactions/income.html', context)


@login_required(login_url='login')
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.income_user = request.user
            instance.save()
            return redirect('manage_income')
        else:
            return render(request, 'transport/demo/pages/transactions/income.html', {'form': form})


@login_required(login_url='login')
def delete_income(request, id):
    income = Income.objects.get(pk=id)
    income.delete()
    return redirect('manage_income')


@login_required(login_url='login')
def manage_expense(request):
    form = ExpenseForm()
    data = Expense.objects.all()
    context = {
        'form': form,
        'data': data,
    }
    return render(request, 'transport/demo/pages/transactions/expense.html', context)


@login_required(login_url='login')
def add_expense(request):
     if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.expense_user = request.user
            instance.save()
            return redirect('manage_expense')
        else:
            return render(request, 'transport/demo/pages/transactions/expense.html', {'form': form})


@login_required(login_url='login')
def delete_expense(request):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    return redirect('manage_expense')


@login_required(login_url='login')
def new_booking(request):
    if request.method == "GET":
        form = BookingForm()
        return render(request, 'transport/demo/pages/bookings/create-booking.html', {'form': form})
    else:
        form = BookingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False) 
            instance.status = "Not Completed"
            instance.payment = 0.0
            instance.save()
            return redirect('manage_booking')
        else:
            return render(request, 'transport/demo/pages/bookings/create-booking.html', {'form': form})

@login_required(login_url='login')
def manage_booking(request):
    data = Bookings.objects.all()
    return render(request, 'transport/demo/pages/bookings/index.html', {'data': data})


@login_required(login_url='login')
def edit_booking(request, id):
    booking = Bookings.objects.get(pk=id)
    if request.method == "GET":
        form = BookingForm(instance=booking)
        return render(request, 'transport/demo/pages/bookings/edit-booking.html', {'form': form})
    else:
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('manage_booking')
        else:
            return render(request, 'transport/demo/pages/bookings/edit-booking.html', {'form': form})


@login_required(login_url='login')
def delete_booking(request, id):
    booking = Bookings.objects.get(pk=id)
    booking.delete()
    return redirect('manage_booking')


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
def update_fuel(request):
    pass


@login_required(login_url='login')
def delete_fuel(request):
    pass


@login_required(login_url='login')
def fuel_history(request):
    data = Fuel.objects.all()
    cost_list = []
    for da in data:
        cost_list.append(da.qty * da.cost_per_unit)

    my_cost = zip(data, cost_list)
    context = {
        'data' : data,
        'cost_list' : cost_list,
        'my_cost' : my_cost,
    }

    return render(request, "transport/demo/pages/fuel/index.html", context)

@login_required(login_url='login')
def add_vendor(request):
    if request.method == "GET":
        form = VendorForm()
        return render(request, "transport/demo/pages/vendors/create-vendor.html", {'form':form})
    else:
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_vendor')
        else: 
            return render(request, "transport/demo/pages/vendors/create-vendor.html", {'form':form})


@login_required(login_url='login')
def manage_vendor(request):
    data = Vendors.objects.all()
    return render(request, "transport/demo/pages/vendors/index.html", {'data':data})


@login_required(login_url='login')
def update_vendor(request, id):
    vendor = Vendors.objects.get(pk=id)
    if request.method == "GET":
        form = VendorForm(instance=vendor)
        return render(request, "transport/demo/pages/vendors/create-vendor.html", {'form': form})
    else:
        form = VendorForm(request.POST, request.FILES, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('manage_vendor')
        else:
            return render(request, "transport/demo/pages/vendors/create-vendor.html", {'form': form})



@login_required(login_url='login')
def delete_vendor(request, id):
    vendor = Vendors.objects.get(pk=id)
    vendor.delete()
    return redirect('manage_vendor')



@login_required(login_url='login')
def manage_workorder(request):
    data = WorkOrders.objects.all()
    return render(request, "transport/demo/pages/workorders/manageworkorders.html", {'data':data})


@login_required(login_url='login')
def add_workorder(request):
    if request.method == "GET":
        form = WorkOrderForm()
        return render(request, 'transport/demo/pages/workorders/create-workorder.html', {'form': form})
    else:
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_workorder')
        else:
            return render(request, 'transport/demo/pages/workorders/create-workorder.html', {'form': form})


@login_required(login_url='login')
def update_workorder(request, id):
    workorder = WorkOrders.objects.get(pk=id)
    if request.method == POST:
        form = WorkOrderForm(request.POST, instance=workorder)
        if form.is_valid():
            form.save()
            return redirect('manage_workorder')
        else:
            return render(request, 'transport/demo/pages/workorders/create-workorder.html', {'form': form})
    else:
        form = WorkOrderForm(request.POST)
        return render(request, 'transport/demo/pages/workorders/create-workorder.html', {'form': form})



@login_required(login_url='login')
def delete_workorder(request, id):
    workorder = WorkOrders.objects.get(pk=id)
    workorder.delete()
    return redirect('manage_workorders')
    


@login_required(login_url='login')
def add_note(request):
    if request.method == "GET":
        form = NoteForm()
        return render(request, "transport/demo/pages/notes/create-note.html", {'form': form})
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_note')
        return render(request, 'transport/demo/pages/notes/create-note.html', {'form': form})


@login_required(login_url='login')
def update_note(request, id):
    note = Notes.objects.get(pk=id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('manage_note')
        else:
            return render(request, 'transport/demo/pages/notes/create-note.html', {'form': form})
    else:
        form = NoteForm(instance=note)
        return render(request, 'transport/demo/pages/notes/create-note.html', {'form': form})


@login_required(login_url='login')
def delete_note(request, id):
    note = Notes.objects.get(pk=id)
    note.delete()
    return redirect('manage_note')



@login_required(login_url='login')
def manage_note(request):
    data = Notes.objects.all()
    return render(request, "transport/demo/pages/notes/index.html", {'data':data})


@login_required(login_url='login')
def manage_reminder(request):
    data = ServiceReminder.objects.all()
    time_list = []
    for da in data:
        time_list.append(da.last_date + timedelta(days=int(da.sr_service.overdue_time)))

    my_list = zip(data, time_list)

    context = {
        'data': data,
        'time_list': time_list,
        'my_list': my_list,
    }
    return render(request, "transport/demo/pages/service-reminder/index.html", context)


@login_required(login_url='login')
def add_reminder(request):
    if request.method == "GET":
        form = ReminderForm()
        items = ServiceItems.objects.all()
        return render(request,  "transport/demo/pages/service-reminder/create-reminder.html", {
            'form': form,
            'items': items,
            })
    else:
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_reminder')
        else:
            return render(request, "transport/demo/pages/service-reminder/create-reminder.html", {'form': form})


@login_required(login_url='login')
def update_reminder(request, id):
    reminder = ServiceReminder.objects.get(pk=id)
    if request.method == "GET":
        form = ReminderForm(instance=reminder)
        return render(request,  "transport/demo/pages/service-reminder/create-reminder.html", {'form': form})
    else:
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('manage_reminder')
        else:
            return render(request,  "transport/demo/pages/service-reminder/create-reminder.html", {'form': form})



@login_required(login_url='login')
def delete_reminder(request, id):
    reminder = ServiceReminder.objects.get(pk=id)
    reminder.delete()
    return redirect('manage_reminder')


@login_required(login_url='login')
def service_item(request):
    data = ServiceItems.objects.all()
    return render(request, "transport/demo/pages/service-reminder/service-items.html", {'data': data})


@login_required(login_url='login')
def add_service_item(request):
    if request.method == "GET":
        form = ServiceItemForm()
        return render(request, "transport/demo/pages/service-reminder/add-service-item.html", {'form': form})
    else:
        form = ServiceItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_item')
        else:
            return render(request, "transport/demo/pages/service-reminder/add-service-item.html", {'form': form})


@login_required(login_url='login')
def update_service_item(request, id):
    item = ServiceItems.objects.get(pk=id)
    if request.method == "GET":
        form = ServiceItemForm(instance = item)
        return render(request, "transport/demo/pages/service-reminder/add-service-item.html", {'form': form})
    else:
        form = ServiceItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save
            return redirect('service_item')


@login_required(login_url='login')
def delete_service_item(request, id):
    item = ServiceItems.objects.get(pk=id)
    item.delete()
    return redirect('service_item')

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
    data = FareSettings.objects.all()
    return render(request,"transport/demo/pages/settings/fare-settings.html", {'data': data})


@login_required(login_url='login')
def expense_categories(request):
    pass

@login_required(login_url='login')
def income_categories(request):
    pass

