from django.contrib import admin
from .models import reserver
# Register your models here.

class reserveration(admin.ModelAdmin):
    list_display = ('id','name','email','check_in','check_out')
    list_display_links = ('id','name','email')

admin.site.register(reserver,reserveration)