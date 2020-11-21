"""Declare URLs."""

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path("", csrf_exempt(views.home), name="home"),
    path("start/", csrf_exempt(views.start), name="start"),
    path("break/", csrf_exempt(views.start_break), name="break"),
]
