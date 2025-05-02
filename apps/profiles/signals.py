import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from real_estate.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile

logger = logging.getLogger(__name__)
@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a user profile when a new user is created.
    """
    if created:
        Profile.objects.create(user=instance)
    #     logger.info(f"Profile created for user: {instance.username}")
    # else:
    #     logger.info(f"Profile already exists for user: {instance.username}")
    
@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to save the user profile when the user is saved.
    """
    instance.profile.save()
    logger.info(f"Profile saved for user: {instance.username}")