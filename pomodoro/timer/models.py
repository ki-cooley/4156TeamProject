from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    #id (primary key) is automatically added
    start_day = models.DateField()
    start_time = models.TimeField()
    end_day = models.DateField()
    end_time = models.TimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class SessionActivity(models.Model):
    #id (primary key) is automatically added
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    site_url = models.URLField()
    visit_timestamp = models.DateTimeField()

class BlockedSite(models.Model):
    #id (primary key) is automatically added
    site_url = models.URLField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
