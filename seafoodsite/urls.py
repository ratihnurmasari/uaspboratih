"""seafoodsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from seafoodapp.views import beranda, abalon, seap, bulbab, sw, kepiting, gurita,tambah_sea, update_sea, delete_sea

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beranda/', beranda),
    path('abalon/', abalon),
    path('seap/', seap),
    path('bulbab/', bulbab),
    path('sw/', sw),
    path('kepiting/', kepiting),
    path('gurita/', gurita),
    path('tambah_sea/', tambah_sea),
    path('foods/update_sea/<int:id_foods>', update_sea, name='update_sea'),
    path('foods/delete_sea/<int:id_foods>', delete_sea, name='delete_sea'),
] 

