from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from . import views

router = routers.DefaultRouter()
router.register(r'session', views.TimerSessionAPI, basename='timer')
router.register(r'sessionactivity', views.TimerSessionActivityAPI)
router.register(r'blockedsite', views.TimerBlockedSiteAPI)



urlpatterns = [
	path('home/', csrf_exempt(views.dashboardHome), name='dashboard-home'),
	path('summary/', csrf_exempt(views.sessionSummary), name='summary'),
	path('detail/<pk>', views.detail, name='detail'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]