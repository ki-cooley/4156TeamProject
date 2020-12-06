from django.shortcuts import render
from rest_framework import viewsets
from django.db import connection, transaction
from .serializers import *
import datetime
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response

# class DashboardAPI(viewsets.ModelViewSet):
# 	serializer_class = DashboardSerializer
# 	queryset = UserDashboard.objects.raw("SELECT * FROM user_dashboard")

# class DashboardWeeklyAPI(viewsets.ModelViewSet):
# 	serializer_class = DashboardSerializer
# 	start_date = datetime.datetime.now() + datetime.timedelta(-7)
# 	queryset = UserDashboard.objects.filter(time__range=(start_date, datetime.datetime.now()))

class TimerSessionAPI(viewsets.ModelViewSet):
	queryset = TimerSession.objects.all()
	serializer_class = TimerSessionSerializer

	@action(methods=['get'], detail=True, url_path='all', url_name='all-session')
	def getUserTimerSession(self, request, pk=None):
		allData = TimerSession.objects.filter(user_id = pk)
		serializer = TimerSessionSerializer(allData, many=True)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='week', url_name='weekly-session')
	def getWeeklyTimerSession(self, request, pk=None):
		start_date = datetime.datetime.now() - datetime.timedelta(days=7)
		lastWeek = TimerSession.objects.filter(start_time__range=(start_date, datetime.datetime.now()), user_id=pk)
		serializer = TimerSessionSerializer(lastWeek, many=True)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='month', url_name='monthly-session')
	def getMonthlySession(self, request, pk=None):
		start_date = datetime.datetime.now() - datetime.timedelta(days=30)
		lastMonth = TimerSession.objects.filter(start_time__range=(start_date, datetime.datetime.now()), user_id=pk)
		serializer = TimerSessionSerializer(lastMonth, many=True)
		return Response(serializer.data)

class TimerSessionActivityAPI(viewsets.ModelViewSet):
	queryset = TimerSessionactivity.objects.all()

	@action(methods=['get'], detail=True, url_path='all', url_name='all-session-activity')
	def getUserTimerSessionActivity(self, request, pk=None):
		allData = TimerSessionactivity.objects.filter(user_id=pk)
		serializer = TimerSessionactivitySerializer(allData, many=True)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='week', url_name='weekly-session-activity')
	def getWeeklyTimerSessionActivity(self, request, pk=None):
		start_date = datetime.datetime.now() - datetime.timedelta(days=7)
		lastWeek = TimerSessionactivity.objects.filter(start_time__range=(start_date, datetime.datetime.now()), user_id=pk)
		serializer = TimerSessionactivitySerializer(lastWeek, many=True)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='month', url_name='monthly-session-activity')
	def getMonthlySessionActivity(self, request, pk=None):
		start_date = datetime.datetime.now() - datetime.timedelta(days=30)
		lastMonth = TimerSessionactivity.objects.filter(start_time__range=(start_date, datetime.datetime.now()), user_id=pk)
		serializer = TimerSessionactivitySerializer(lastMonth, many=True)
		return Response(serializer.data)

class TimerBlockedSiteAPI(viewsets.ModelViewSet):
	queryset = TimerBlockedsite.objects.all()

	@action(methods=['get'], detail=True, url_path='', url_name='all-blocked-site')
	def getUserTimerBlockedsite(self, request, pk=None):
		allData = TimerBlockedsite.objects.all(user_id_id=pk)
		serializer = TimerBlockedsiteSerializer(allData, many=True)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='week', url_name='weekly-blocked-site')
	def getWeeklyTimerBlockedsite(self, request, pk=None):
		start_date = datetime.datetime.now() - datetime.timedelta(days=7)
		lastWeek = TimerBlockedsite.objects.filter(time__range=(start_date, datetime.datetime.now()), user_id=pk)
		serializer = TimerBlockedsiteSerializer(lastWeek, many=True)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='month', url_name='monthly-blocked-site')
	def getMonthlyTimerBlockedsite(self, request, pk=None):
		start_date = datetime.datetime.now() - datetime.timedelta(days=30)
		lastMonth = TimerBlockedsite.objects.filter(time__range=(start_date, datetime.datetime.now()), user_id=pk)
		serializer = TimerBlockedsiteSerializer(lastMonth, many=True)
		return Response(serializer.data)

