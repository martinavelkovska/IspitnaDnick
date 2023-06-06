from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Kategorija(models.Model):
    ime = models.CharField(max_length=20)
    opis = models.TextField()
    active = models.BooleanField()
   # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ime

class Product(models.Model):
    code = models.AutoField( primary_key=True)
    ime = models.CharField(max_length=35)
    opis = models.TextField(null=True, blank=True)
    photo = models.FileField("files/", blank=True, null=True)
    cena = models.IntegerField()
    kolicina = models.IntegerField()
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Klient(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=20)
    adresa = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class Prodazba(models.Model):
    produkti = models.ForeignKey(Product, on_delete=models.CASCADE)
    datum_prodazba = models.DateField(auto_now=True)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE,null=True, blank=True)
