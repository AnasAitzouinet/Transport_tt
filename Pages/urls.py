from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('home',views.home, name="home"),
    
]