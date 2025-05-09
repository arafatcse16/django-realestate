from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=["id","pkid","user","gender","phone_number","country","city"]
    list_filter=["gender","country","city"]
    search_fields=["id","pkid","user"]
    
admin.site.register(Profile, ProfileAdmin)