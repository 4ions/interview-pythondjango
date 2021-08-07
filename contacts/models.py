from django.db import models
from django.forms import ModelForm, Textarea
# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

class Enterprise(models.Model):
    owner_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    nameC = models.CharField(max_length=100)
    descrip = models.CharField(max_length=1000)
    price = models.IntegerField()
    adress = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)

    def __str__(self):
        return self.nameC
