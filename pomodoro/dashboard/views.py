from django.shortcuts import render
from rest_framework import viewsets
from django.db import connection, transaction
from .serializers import *
import datetime
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response

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

class UserViewSet(viewsets.ModelViewSet):
	queryset = UserDashboard.objects.all()
	@action(methods=['get'], detail=True, url_path='week', url_name='weekly-dashboard')
	def getWeeklyDashboard(self, request, pk=None):
		start_date = datetime.datetime.now() - datetime.timedelta(days=7)
		lastWeek = UserDashboard.objects.filter(time__range=(start_date, datetime.datetime.now()), pk=pk)
		serializer = DashboardSerializer(lastWeek, many=True)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='month', url_name='monthly-dashboard')
	def getWeeklyDashboard(self, request, pk=None):
		start_date = datetime.datetime.now() - datetime.timedelta(days=30)
		lastWeek = UserDashboard.objects.filter(time__range=(start_date, datetime.datetime.now()), pk=pk)
		serializer = DashboardSerializer(lastWeek, many=True)
		return Response(serializer.data)
