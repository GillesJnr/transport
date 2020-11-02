"""cagltransport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
=======
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
>>>>>>> 6b4de6aef6f281aa932af2f795ad7357155b6999
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
=======
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('transport/', include('transport.urls')),
>>>>>>> 6b4de6aef6f281aa932af2f795ad7357155b6999
]
