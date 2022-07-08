from datetime import datetime
from distutils.command.upload import upload
from pickle import TRUE
from zoneinfo import available_timezones
from django.db import models
from django.forms import CharField
from PIL import Image
from django.core.exceptions import ValidationError
from django.db.models.fields.files import ImageField, ImageFieldFile



# Create your models here.
class Listings(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    adresse = models.CharField(max_length=200)
    description = models.TextField()
    availablecheck_in = models.DateTimeField(default=datetime.now())
    availablecheck_out = models.DateTimeField(default=datetime.now())
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField('photo_main',upload_to='photos/%Y/%m/%d/')
    photo_main1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=TRUE)
    photo_main2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=TRUE)
    photo_main3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=TRUE)
    photo_main4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=TRUE)
    review = models.DecimalField(max_digits=5, decimal_places=1)
    
    def __str__(self) :
        return self.title 

class excursion_add(models.Model):
    excursion_add = models.CharField(max_length=200)
    def __str__(self) :
        return self.excursion_add

class cars_add(models.Model):
    cars_add = models.CharField(max_length=200)
    def __str__(self) :
        return self.cars_add 
        
class availablecheck(models.Model):
    availablecheck_inadd = models.DateTimeField(default=datetime.now())
    availablecheck_outadd = models.DateTimeField(default=datetime.now())
    def __str__(self) :
        return self.availablecheck_inadd 

