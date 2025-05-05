from django.contrib import admin
from .models import Property,PropertyViews

class PropertyAdmin(admin.ModelAdmin):
    ist_display = ["title", "country", "advert_type", "property_type"]
    list_filter = ["advert_type", "property_type", "country"]
    
    
admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyViews)