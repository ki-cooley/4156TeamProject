from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'month', views.DashboardMonthlyAPI)
router.register(r'week', views.DashboardWeeklyAPI)
router.register(r'user', views.UserViewSet)
router.register(r'', views.DashboardAPI)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]