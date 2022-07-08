from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('all_hotels',views.all_hotels, name="all_hotels"),
    path('<int:hotel_id>',views.hotel,name='hotel'),
]