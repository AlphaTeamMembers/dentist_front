from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

from app.models import Profile


def Create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(
            user=user,
            username=user.username,
        )


def Delete(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print('deleted', user)


post_save.connect(Create_profile, sender=User)

post_delete.connect(Delete, sender=Profile)
