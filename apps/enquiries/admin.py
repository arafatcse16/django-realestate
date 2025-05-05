from django.contrib import admin

from .models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):
    list_display=["name", "phone_number", "email", "subject", "message"]
    
admin.site.register(Enquiry, EnquiryAdmin)
