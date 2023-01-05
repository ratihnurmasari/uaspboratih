from django.forms import ModelForm
from django import forms
from seafoodapp.models import *

class Formseafood(ModelForm):
    class Meta:
        model = seafood
        fields = '__all__'
        
        widgets = {
            'nama' : forms.TextInput({'class' : 'form-control', 'placeholder' : 'Masukan nama seafood'} ),

            'kingdom' : forms.TextInput({'class' : 'form-control', 'placeholder' : 'Masukan bagian kingdom'} ),

            'filum_id' : forms.Select({'class' : 'form-control'} ),

            'kelas' : forms.TextInput({'class' : 'form-control', 'placeholder' : 'Masukan kelas seafood'} ),

            'image' : forms.TextInput({'class' : 'form-control', 'placeholder' : 'Masukan gambar seafood'} ),

            'detail' : forms.TextInput({'class' : 'form-control', 'placeholder' : 'isi oleh admin'} ),
        }

class Formmap(ModelForm):
    class Meta:
        model = map
        fields = '__all__'
        
        widgets = {
            'nama_tempat' : forms.TextInput({'class' : 'form-control', 'placeholder' : 'Masukan nama tempat'} ),

            'koordinat' : forms.TextInput({'class' : 'form-control', 'placeholder' : 'Masukan koordinat'} ),
        }