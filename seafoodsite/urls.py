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
from seafoodapp import views
from seafoodapp.views import beranda, abalon, seap, bulbab, sw, kepiting, gurita,tambah_sea, update_sea, delete_sea, index, register, login, lokasi, tambah_map, update_map, delete_map

urlpatterns = [
    path('admin/', admin.site.urls),
        path('register/',views.register , name='register'),
    path('login/',views.login , name='login'),
    path('logout/',views.logoutUser , name='logout'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('beranda/', beranda),
    path('lokasi/', views.lokasi, name='lokasi'),
    path('index/', views.index, name="index"),
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
    path('tambah_map/', tambah_map),
    path('maps/update_map/<int:id_maps>', update_map, name='update_map'),
    path('maps/delete_map/<int:id_maps>', delete_map, name='delete_map'),
] 

