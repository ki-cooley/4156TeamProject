from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.db import connection, transaction
from django.contrib.auth.decorators import login_required
from .serializers import *
import datetime
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
import requests

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
		lastWeek = TimerSessionactivity.objects.filter(visit_timestamp__range=(start_date, datetime.datetime.now()), user_id=pk)
		serializer = TimerSessionactivitySerializer(lastWeek, many=True)
		return Response(serializer.data)

	@action(methods=['get'], detail=True, url_path='month', url_name='monthly-session-activity')
	def getMonthlySessionActivity(self, request, pk=None):
		start_date = datetime.datetime.now() - datetime.timedelta(days=30)
		lastMonth = TimerSessionactivity.objects.filter(visit_timestamp__range=(start_date, datetime.datetime.now()), user_id=pk)
		serializer = TimerSessionactivitySerializer(lastMonth, many=True)
		return Response(serializer.data)

class TimerBlockedSiteAPI(viewsets.ModelViewSet):
	queryset = TimerBlockedsite.objects.all()

	@action(methods=['get'], detail=True, url_path='all', url_name='all-blocked-site')
	def getUserTimerBlockedsite(self, request, pk=None):
		allData = TimerBlockedsite.objects.filter(user_id=pk)
		serializer = TimerBlockedsiteSerializer(allData, many=True)
		return Response(serializer.data)


@login_required
def dashboardHome(request):
	user_data = sessionSummary(request)
	return render(request, "dashboard_home.html", {"all_items" : user_data})

@login_required
def sessionSummary(request):
    if request.user.is_authenticated:
         allData = TimerSession.objects.filter(user_id = request.user.id)
         return allData
    else:
    	return None

@login_required
def detail(request, pk):
	if request.user.is_authenticated:
		sessionData = TimerSession.objects.filter(user_id=request.user.id, id=pk)
		if len(sessionData) == 0 : 
			return render(request, "detail.html", {"session_data" : None,
			"activity_data": None, 
			"blockedsites_data": None})
		start, end = (sessionData[0].start_time, sessionData[0].end_time)
		activityData = TimerSessionactivity.objects.filter(user_id=request.user.id, visit_timestamp__range= (start-datetime.timedelta(hours = 5), end-datetime.timedelta(hours = 5)))
		blockedsitesData = TimerBlockedsite.objects.filter(user_id=request.user.id)

		return render(request, "detail.html", {"session_data" : sessionData,
			"activity_data": activityData, 
			"blockedsites_data": blockedsitesData})


