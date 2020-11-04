from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name="home"),
    path('adduser', views.adduser, name="adduser"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name = "logout"),
    path('customers', views.view_customers, name="view_customers"),
    path('users', views.view_users, name="view_users"),
    path('drivers', views.view_drivers, name="view_drivers"),
]
