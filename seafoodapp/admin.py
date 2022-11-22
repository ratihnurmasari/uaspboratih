from django.contrib import admin
from .models import *
# Register your models here.
class seafoodAdmin(admin.ModelAdmin):
    list_display = ('nama', 'filum_id', 'image')

admin.site.register(seafood,seafoodAdmin)
admin.site.register(Kelompok)