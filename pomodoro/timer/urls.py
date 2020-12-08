"""Declare URLs."""
from django.urls import path, include
from . import views, pomodoro_timer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'track', views.SessionActivityViewSet)
router.register(r'block', views.BlockedSiteViewSet, basename='blockedsite')
router.register(r'session', views.SessionViewSet, basename='session')

urlpatterns = [
    path("", csrf_exempt(views.home), name="home"),
    path("start/", csrf_exempt(views.start), name="start"),
    path("break/", csrf_exempt(views.start_break), name="break"),
    path("api/", include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
