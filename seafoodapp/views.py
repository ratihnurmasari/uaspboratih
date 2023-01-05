from django.shortcuts import render, redirect
from seafoodapp.models import *
from seafoodapp.forms import *
from django.contrib.auth import  authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as authlogin
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form =UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Akun anda sudah dibuat ' + user)
                return redirect('login')

    data ={'form':form}
    return render(request,'accounts/register.html', data)

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password )

            if user is not None:
                authlogin(request, user)
                return redirect ('index')
            else:
                messages.info(request, 'Username atau Password salah ')
    data ={}
    return render(request, 'accounts/login.html', data )

def logoutUser(request):
    logout(request)
    messages.info(request,'Anda berhasil keluar')
    return redirect('login')

@login_required(login_url='login')
def beranda(request):
    foods= seafood.objects.all()
    data= {
        'Title' : "Seafood",
        'Heading' : "Informasi Mengenai Seafood",
        'foods' : foods,
    }
    return render(request, 'beranda.html', data)

@login_required(login_url='login')
def index(request):
    foods= seafood.objects.all()
    maps = map.objects.all()
    data= {
        'Title' : "Selamat Datang",
        'maps' :maps,
        'foods' : foods,
    }
    return render(request, 'index.html', data)

@login_required(login_url='login')
def lokasi(request):
    maps = map.objects.all()
    data= {
        'Title' : "Lokasi",
        'maps': maps,
    }

    return render(request, 'lokasi.html', data)
 
@login_required(login_url='login')
def beranda(request):
    foods= seafood.objects.all()
    data= {
        'Title' : "Beranda",
        'Heading' : "Selamat Datang",
        'foods' : foods,
    }
    return render(request, 'beranda.html', data)

@login_required(login_url='login')
def abalon(request):
    data= {
        'Title' : "Abalon",
        'Heading' : "Profil abalon",
    }
    return render(request, 'abalon.html', data)

@login_required(login_url='login')
def seap(request):
    data= {
        'Title' : "sea pineapple",
        'Heading' : "Profil Sea pineapple",
    }
    return render(request, 'seap.html', data)

@login_required(login_url='login')
def bulbab(request):
    data= {
        'Title' : "Bulu Babi",
        'Heading' : "Profil Bulu Babi",
    }
    return render(request, 'bulbab.html', data)

@login_required(login_url='login')
def sw(request):
    data= {
        'Title' : "Spoon Worm",
        'Heading' : "Profil Spoon Worm",
    }
    return render(request, 'sw.html', data)

@login_required(login_url='login')
def kepiting(request):
    data= {
        'Title' : "Kepiting",
        'Heading' : "Profil Kepiting",
    }
    return render(request, 'kepiting.html', data)

@login_required(login_url='login')
def gurita(request):
    data= {
        'Title' : "Gurita",
        'Heading' : "Profil Gurita",
    }
    return render(request, 'gurita.html', data)

@login_required(login_url='login')
def tambah_sea(request):
    if request.POST:
        form = Formseafood(request.POST)
        if form.is_valid():
            form.save()
            form = Formseafood()
            data= {
            'Title' : "Tambah data Seafood",
            'Heading' : "Tambah data Seafood",
            'form' : form,
            'pesan': "Data berhasil ditambahkan",
              }
            return render(request, 'tambah_sea.html', data)
    else:
        form = Formseafood()
        data= {
            'Title' : "Tambah data Seafood",
            'Heading' : "Tambah data Seafood",
            'form' : form,
        }
    return render(request, 'tambah_sea.html', data)


def update_sea(request, id_foods):
    foods = seafood.objects.get (id = id_foods)
    
    if request.POST:
        form = Formseafood(request.POST, instance=foods)
        if form.is_valid():
            form.save()
            form = Formseafood()
            data= {
                'Title' : "Update data Seafood",
                'Heading' : "Update data Seafood",
                'form' : form,
                'pesan': "Data berhasil diupdate",
                'foods' : foods, 
                'seafood' : seafood,
            }
            return render(request, 'update_sea.html', data)

    else:
        form = Formseafood(instance=foods)
        data= {
            'Title' : "Edit data",
            'form' : form,
            'foods' : foods,
            } 
    return render(request, 'update_sea.html', data)

def delete_sea(request, id_foods):
    foods = seafood.objects.get (id = id_foods)
    foods.delete()

    return redirect('/beranda/')

#map
def tambah_map(request):
    if request.POST:
        form = Formmap(request.POST)
        if form.is_valid():
            form.save()
            form = Formmap()
            data= {
            'Title' : "Tambah data Map",
            'Heading' : "Tambah data Map",
            'form' : form,
            'pesan': "Data berhasil ditambahkan",
              }
            return render(request, 'tambah_map.html', data)
    else:
        form = Formmap()
        data= {
            'Title' : "Tambah data Map",
            'Heading' : "Tambah data Map",
            'form' : form,
        }
    return render(request, 'tambah_map.html', data)

def update_map(request, id_maps):
    maps = map.objects.get (id = id_maps)
    if request.POST:
        form = Formmap(request.POST, instance=maps)
        if form.is_valid():
            form.save()
            form = Formmap()
            data= {
                'Title' : "Update data Seafood",
                'Heading' : "Update data Seafood",
                'form' : form,
                'pesan': "Data berhasil diupdate",
                'maps' : maps, 
                'map' : map,
            }
            return render(request, 'update_map.html', data)

    else:
        form = Formmap(instance=maps)
        data= {
            'Title' : "Edit data",
            'form' : form,
            'maps' : maps, 
            } 
    return render(request, 'update_map.html', data)

def delete_map(request, id_maps):
    maps = map.objects.get (id = id_maps)
    maps.delete()

    return redirect('/lokasi/')