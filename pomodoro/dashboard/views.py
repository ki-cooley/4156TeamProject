from django.shortcuts import render
from rest_framework import viewsets
from django.db import connection, transaction
from .serializers import *
import datetime
from django.utils import timezone


class DashboardAPI(viewsets.ModelViewSet):
	serializer_class = DashboardSerializer
	queryset = UserDashboard.objects.raw("SELECT * FROM user_dashboard")

class DashboardWeeklyAPI(viewsets.ModelViewSet):
	serializer_class = DashboardSerializer
	start_date = datetime.datetime.now() + datetime.timedelta(-7)
	queryset = UserDashboard.objects.filter(time__range=(start_date, datetime.datetime.now()))

class DashboardMonthlyAPI(viewsets.ModelViewSet):
	serializer_class = DashboardSerializer
	start_date = datetime.datetime.now() + datetime.timedelta(-30)
	queryset = UserDashboard.objects.filter(time__range=(start_date, datetime.datetime.now()))