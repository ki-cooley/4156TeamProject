"""DB tables."""
from django.contrib.auth.models import User
from django.db import models


class Session(models.Model):
    """Session table that stores."""
    # id (primary key) is automatically added
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class SessionActivity(models.Model):
    """Session activity table."""
    # id (primary key) is automatically added
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    site_url = models.URLField()
    visit_timestamp = models.DateTimeField()


class BlockedSite(models.Model):
    """Session activity table."""
    # id (primary key) is automatically added
    site_url = models.URLField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
