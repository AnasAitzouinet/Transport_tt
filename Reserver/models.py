from http import client
from pickle import TRUE
from pyexpat import model
from re import M
from unicodedata import name
from urllib import request
from django.db import models
from django.contrib import messages,auth

from django.contrib.auth.models import User
# Create your models here.
class reserver(models.Model):
    name = models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)
    check_in = models.DateTimeField()
    check_out= models.DateTimeField()
    adults = models.IntegerField()
    phone = models.IntegerField(null=TRUE)
    kids = models.IntegerField()
    email = models.EmailField()
    streetline_1 = models.CharField(max_length=220)
    streetline_2 = models.CharField(blank=True,max_length=220)
    city = models.CharField(max_length=100)
    state = models.CharField(blank=True,max_length=220)
    zip_code = models.IntegerField()
    details = models.TextField(blank=TRUE)
    excursion  = models.CharField(max_length=200)
    cars  = models.CharField(max_length=200)
    
    def __str__(self) :
        return  self.name 
