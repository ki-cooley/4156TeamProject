from django.urls import path
from . import views, pomodoro_timer
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("", csrf_exempt(views.output), name="home"),
    path("login/", csrf_exempt(views.home), name="login"), #to link to login html
    path("start/", csrf_exempt(views.start), name="start"),
]
