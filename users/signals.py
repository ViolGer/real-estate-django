from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.models import Group


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    agent_group, _ = Group.objects.get_or_create(name='Агент')
    instance.groups.add(agent_group)