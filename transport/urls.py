from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name="home"),
    path('adduser', views.adduser, name="adduser"),
    path('login', views.login, name = "login"),
    path('customers', views.view_customers, name="view_customers")

]
