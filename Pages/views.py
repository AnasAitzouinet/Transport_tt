from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from Listings.models import Listings
from Hotels.models import Hotel

# Create your views here.
def index(request):
    template = loader.get_template('Base_Home.html')
    return HttpResponse(template.render({}, request))


    
def home(request):
    data = Listings.objects.all()
    data1 = Hotel.objects.all()

    context= {
            'Listings': data ,
            'Hotel': data1
        }
     
    return render(request,'Pages/Home.html',context)



