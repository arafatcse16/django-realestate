from django.db import models
from django.utils.translation import gettext_lazy as _
from real_estate.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampUUIDModel
from apps.profiles.models import Profile

class Rating(TimeStampUUIDModel):
    class Range(models.IntegerChoices):
        Rating_1 = 1, _("Poor")
        Rating_2 = 2, _("Fair")
        Rating_3 = 3, _("Good")
        Rating_4 = 4, _("Very Good")
        Rating_5 = 5, _("Excellent")
        
    rater=models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name=_("User providing the rating"))
    agent=models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name="agent_review", null=True, verbose_name=_("Agent being rated"))
    rating=models.IntegerField(choices=Range.choices, default=0, verbose_name=_("Rating"), help_text="1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent")
    comment=models.TextField(verbose_name=_("Comment"), blank=True, null=True)
    
    class Meta:
        unique_together = ("rater", "agent")        
        
    def __str__(self):
        return f"{self.agent} rated at {self.rating}"
    
    