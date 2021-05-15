from django.db import models

# Create your models here.


class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField
    offer = models.BooleanField(default=False)


class Package(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Destination = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    Date = models.TextField()
    Phoneno = models.TextField()
    offer = models.BooleanField(default=False)
