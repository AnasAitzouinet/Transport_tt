from multiprocessing import context
from django.shortcuts import render
from .models import Listings

# Create your views here.

def Listings(request,Listings_id):
    return render(request,'Pages/all_hotels.html')

