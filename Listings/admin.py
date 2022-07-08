from django.contrib import admin
from .models import Listings, excursion_add,cars_add,availablecheck
# Register your models here.

class listingadmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price')
    list_display_links = ('id','title')

admin.site.register(cars_add)
admin.site.register(availablecheck)
admin.site.register(excursion_add)
admin.site.register(Listings,listingadmin)
