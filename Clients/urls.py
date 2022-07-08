from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout,name="logout"),

]