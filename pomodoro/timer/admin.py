from django.contrib import admin
from .models import Session, SessionActivity, BlockedSite

# Register your models here.
admin.site.register(Session)
admin.site.register(SessionActivity)
admin.site.register(BlockedSite)