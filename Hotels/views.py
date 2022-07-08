from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import Hotel
# Create your views here.

def all_hotels(request):
    data1 = Hotel.objects.all()
    context={
            'Hotel': data1
    }
    return render(request,'Pages/all_hotels.html',context)

def hotel(request,hotel_id):
    hotels = get_object_or_404(Hotel,pk=hotel_id)
    context={
        'hotels':hotels
    }
    return render(request,'Pages/single_hotel.html',context)
