from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'session', views.TimerSessionAPI)
router.register(r'sessionactivity', views.TimerSessionActivityAPI)
router.register(r'blockedsite', views.TimerBlockedSiteAPI)
# router.register(r'test', views.ExampleViewSet)
# router.register(r'', views.DashboardAPI)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]