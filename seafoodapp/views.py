from django.shortcuts import render, redirect
from seafoodapp.models import *
from seafoodapp.forms import *

# Create your views here.
def beranda(request):
    foods= seafood.objects.all()
    data= {
        'Title' : "Beranda",
        'Heading' : "Selamat Datang",
        'foods' : foods,
    }
    return render(request, 'beranda.html', data)

def abalon(request):
    data= {
        'Title' : "Abalon",
        'Heading' : "Profil abalon",
    }
    return render(request, 'abalon.html', data)

def seap(request):
    data= {
        'Title' : "sea pineapple",
        'Heading' : "Profil Sea pineapple",
    }
    return render(request, 'seap.html', data)

def bulbab(request):
    data= {
        'Title' : "Bulu Babi",
        'Heading' : "Profil Bulu Babi",
    }
    return render(request, 'bulbab.html', data)

def sw(request):
    data= {
        'Title' : "Spoon Worm",
        'Heading' : "Profil Spoon Worm",
    }
    return render(request, 'sw.html', data)

def kepiting(request):
    data= {
        'Title' : "Kepiting",
        'Heading' : "Profil Kepiting",
    }
    return render(request, 'kepiting.html', data)

def gurita(request):
    data= {
        'Title' : "Gurita",
        'Heading' : "Profil Gurita",
    }
    return render(request, 'gurita.html', data)

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