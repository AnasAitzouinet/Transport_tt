from django.contrib import admin
from .models import Hotel
# Register your models here.
class Hoteladmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price')
    list_display_links = ('id','title')
admin.site.register(Hotel,Hoteladmin)