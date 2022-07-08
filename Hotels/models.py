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
class Hotel(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    adresse = models.CharField(max_length=200)
    description = models.TextField()
    availablecheck_in = models.DateTimeField(default=datetime.now())
    bathrooms = models.IntegerField()
    bedrooms = models.IntegerField()
    rooms = models.IntegerField()
    photo_main = models.ImageField('photo_main',upload_to='photos/%Y/%m/%d/')
    photo_main1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=TRUE)
    photo_main2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=TRUE)
    photo_main3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=TRUE)
    photo_main4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=TRUE)
    review = models.DecimalField(max_digits=5, decimal_places=1)
    Pools = models.BooleanField(default=True)
    wifi = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
   
    def __str__(self) :
        return self.title 
