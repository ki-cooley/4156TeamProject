"""View test example."""
from django.test import TestCase
import pytest
from unittest import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse, resolve
from mixer.backend.django import mixer
from dashboard import views as v
from dashboard.models import *
import datetime
from django.utils import timezone


@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        cls.factory = RequestFactory()

    def test_dashboard_home_authenticated(self):
        path = reverse('dashboard-home', kwargs={})
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        response = v.dashboardHome(request)
        assert response.status_code == 200

    def test_dashboard_home_unauthenticated(self):
        path = reverse('dashboard-home', kwargs={})
        request = self.factory.get(path)

        request.user = AnonymousUser()
        response = v.dashboardHome(request)
        assert response.status_code == 302 # User Not Found Error Code

    def test_dashboard_session_authenticated(self):
        path = reverse('summary', kwargs={})
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        responseData = v.sessionSummary(request)
        actualData = TimerSession.objects.filter(user_id = request.user.id)
        assert len(responseData) == len(actualData)

    def test_dashboard_session_unauthenticated(self):
        path = reverse('summary', kwargs={})
        request = self.factory.get(path)

        request.user = AnonymousUser()
        response = v.sessionSummary(request)
        assert response.status_code == 302 # User Not Found Error Code    

    def test_session_detail_authenticated(self):
        path = reverse('detail', kwargs={'pk' : 100})
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        response = v.detail(request, 50)
        assert response.status_code == 200

    def test_session_detail_unauthenticated(self):
        path = reverse('detail', kwargs={'pk' : 100})
        request = self.factory.get(path)
        request.user = AnonymousUser()
        response = v.detail(request, 50)
        assert response.status_code == 302 # User Not Found Error Code    
    
    def test_timer_session_all_api(self):
        path = 'http://127.0.0.1:8000/dashboard/session/150/all'
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        responseData = v.TimerSessionAPI.getUserTimerSession(request, 150).data
        actualData = TimerSession.objects.filter(user_id = 150)
        assert len(responseData) == len(actualData)

    def test_timer_session_weekly_api(self):
        path = 'http://127.0.0.1:8000/dashboard/session/150/week'
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        responseData = v.TimerSessionAPI.getWeeklyTimerSession(request, 150).data
        start_date = datetime.datetime.now() - datetime.timedelta(days=7)
        actualData = TimerSession.objects.filter(start_time__range=(start_date, datetime.datetime.now()), user_id=150)
        assert len(responseData) == len(actualData)

    def test_timer_session_monthly_api(self):
        path = 'http://127.0.0.1:8000/dashboard/session/150/month'
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        responseData = v.TimerSessionAPI.getMonthlySession(request, 150).data
        start_date = datetime.datetime.now() - datetime.timedelta(days=30)
        actualData = TimerSession.objects.filter(start_time__range=(start_date, datetime.datetime.now()), user_id=150)
        assert len(responseData) == len(actualData)

    def test_timer_session_activity_all_api(self):
        path = 'http://127.0.0.1:8000/dashboard/sessionactivity/150/all'
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        responseData = v.TimerSessionActivityAPI.getUserTimerSessionActivity(request, 150).data
        actualData = TimerSessionactivity.objects.filter(user_id = 150)
        assert len(responseData) == len(actualData)

    def test_timer_session_activity_weekly_api(self):
        path = 'http://127.0.0.1:8000/dashboard/sessionactivity/150/week'
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        responseData = v.TimerSessionActivityAPI.getWeeklyTimerSessionActivity(request, 150).data
        start_date = datetime.datetime.now() - datetime.timedelta(days=7)
        actualData = TimerSessionactivity.objects.filter(visit_timestamp__range=(start_date, datetime.datetime.now()), user_id=150)
        assert len(responseData) == len(actualData)

    def test_timer_session_activity_monthly_api(self):
        path = 'http://127.0.0.1:8000/dashboard/sessionactivity/150/month'
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        responseData = v.TimerSessionActivityAPI.getMonthlySessionActivity(request, 150).data
        start_date = datetime.datetime.now() - datetime.timedelta(days=30)
        actualData = TimerSessionactivity.objects.filter(visit_timestamp__range=(start_date, datetime.datetime.now()), user_id=150)
        assert len(responseData) == len(actualData)

    def test_blocked_sites_all_api(self):
        path = 'http://127.0.0.1:8000/dashboard/blockedsite/150/all'
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        responseData = v.TimerBlockedSiteAPI.getUserTimerBlockedsite(request, 150).data
        actualData = TimerBlockedsite.objects.filter(user_id = 150)
        assert len(responseData) == len(actualData)