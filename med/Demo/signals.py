from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import User_type

@receiver(post_save, sender=User)
def create_user_type(sender, instance, created, **kwargs):
    if created:
        User_type.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_type(sender, instance, **kwargs):
    instance.user_type.save()