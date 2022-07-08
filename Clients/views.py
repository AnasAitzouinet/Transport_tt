from email import message
from django.contrib import messages,auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']
        
        if password == con_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')    
                return redirect('register')
            else:    
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is bein used')    
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,
                    first_name=first_name,last_name=last_name)
                    #auth.login(request,user)
                    user.save()
                    messages.success(request,'You are now Registered ')
                    return redirect('login')
        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')

    else:
        return render(request,'client/register.html')
def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Login Informations')
            return redirect('login')
    else:
        return render(request,'client\login.html')
def dashboard(request):
    return render(request,'client\dashboard.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('home')   
    