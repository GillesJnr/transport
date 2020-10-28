from django.shortcuts import render
from .models import Users
# Create your views here.


def home(request):
    return render(request, "transport/demo/layout.html")

def adduser(request):
    return render(request, "transport/demo/pages/ui-features/adduser.html")

def login(request):
    return render(request, "transport/demo/pages/samples/login.html")

def view_customers(request):
    data = Users.objects.all().filter(user_type='C')
    return render(request, "transport/demo/pages/customers/index.html", {'data':data})