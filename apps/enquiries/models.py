from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampUUIDModel

class Enquiry(TimeStampUUIDModel):
    name=models.CharField(max_length=100, verbose_name=_("Your Name"))
    phone_number=PhoneNumberField(
        verbose_name=_("Your Phone Number"),
        max_length=30, default="+8801712345678",
    )
    email=models.EmailField("Email")
    subject=models.CharField(max_length=100, verbose_name=_("Subject"))
    message=models.TextField(verbose_name=_("Message"))
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Enquiries"