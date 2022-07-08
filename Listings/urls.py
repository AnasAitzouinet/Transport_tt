from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('<int:Listings_id>',views.Listings,name='Listings'),
]