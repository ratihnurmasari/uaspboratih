from distutils.command.upload import upload
from pickle import TRUE
from django.db import models

# Create your models here.
class Kelompok(models.Model):
    filum = models.CharField(max_length=20)
    keterangan = models.TextField()

    def __str__(self):
        return self.filum

class seafood(models.Model):
    nama = models.CharField(max_length=40)
    kingdom = models.CharField(max_length=50)
    filum_id = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)
    kelas = models.CharField(max_length=40)
    image = models.CharField(max_length=50, null=True)
    detail = models.URLField(max_length=100)

    def __str__(self):
        return self.nama
