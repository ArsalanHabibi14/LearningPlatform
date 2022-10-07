from django.db.models.signals import post_delete, post_save
from .models import Profiles
from django.contrib.auth.models import User


def profile_create(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profiles.objects.create(
            user=user,
            username=user.username,
            last_name=user.last_name,
            user_type=3,
            email=user.email
        )


post_save.connect(profile_create, User)


def profile_update(sender, instance, created, **kwargs):
    user = instance
    if created == False:
        profile = Profiles.objects.get(user=user)
        profile.user = user
        profile.username = user.username
        profile.last_name = user.last_name
        profile.user_type = 'stu'
        profile.email = user.email
        profile.save()


post_save.connect(profile_update, User)


def profile_delete(sender, instance, **kwargs):
    user = instance
    profile = Profiles.objects.get(user=user)
    profile.delete()


post_delete.connect(profile_delete, User)
