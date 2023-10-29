from django.db.models.signals import post_save

from django.dispatch import receiver
from EcommerceWebAPI.apps.user.models import CustomUser, ContactUser


@receiver(post_save, sender=CustomUser)
def create_contact_user(sender, instance, created, **kwargs):
    if created:
        ContactUser.objects.create(user=instance, email=instance.email)
