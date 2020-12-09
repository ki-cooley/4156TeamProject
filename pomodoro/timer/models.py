"""DB tables."""
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Session(models.Model):
    """Session table that stores."""
    # id (primary key) is automatically added
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class SessionActivity(models.Model):
    """Session activity table."""
    # id (primary key) is automatically added
    # session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    site_url = models.URLField()
    visit_timestamp = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)


class BlockedSite(models.Model):
    """Session activity table."""
    # id (primary key) is automatically added
    site_url = models.URLField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
