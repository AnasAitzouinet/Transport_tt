from datetime import datetime
import imp
from pyexpat import model
from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import reserver
# Create your views here.

def reservers(request):
    

    if request.method == 'POST':
        x = request.POST['first_name']
        last_name = request.POST['last_name']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        adults = request.POST['adults']
        phone = request.POST['phone']
        kids = request.POST['kids']
        email = request.POST['email']
        streetline_1 = request.POST['streetline_1']
        streetline_2 = request.POST['streetline_2']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        details = request.POST['details']
        excursion = request.POST['excursion']
        cars = request.POST['cars']

        reservations = reserver(name= x,last_name=last_name,check_in=check_in,check_out=check_out,adults=adults,phone=phone,
        kids=kids,email=email,streetline_1=streetline_1,streetline_2=streetline_2,state=state,zip_code=zip_code,details=details,excursion=excursion,cars=cars)
        reservations.save()
        messages.success(request,'Your Reservtion is sent to our Admins, We Will Approch you asap !!! ')
        return redirect('reserver')
    return render(request,'Pages/reserver.html')