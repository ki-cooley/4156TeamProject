"""View test example."""
from django.test import TestCase
import pytest
from unittest import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse, resolve
from mixer.backend.django import mixer
from dashboard import views as v


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
        path = reverse('dashboard-summary', kwargs={})
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        response = v.sessionSummary(request)
        assert response.status_code == 302

    def test_dashboard_session_unauthenticated(self):
        path = reverse('dashboard-summary', kwargs={})
        request = self.factory.get(path)

        request.user = AnonymousUser()
        response = v.sessionSummary(request)
        assert response.status_code == 302 # User Not Found Error Code    

    def test_summary_button(self):
        c = Client()
        response = c.post('/dashboard/home', {'entire_summary': 'summary'})
        print("STATUS IS " + str(response.status_code))
        self.assertEqual(response.status_code, 301)

    def test_activity_button(self):
        c = Client()
        response = c.post('/dashboard/home', {'entire_summary': 'activity'})
        print("STATUS IS " + str(response.status_code))
        self.assertEqual(response.status_code, 301)    

    def test_blocked_button(self):
        c = Client()
        response = c.post('/dashboard/home', {'entire_summary': 'blocked'})
        print("STATUS IS " + str(response.status_code))
        self.assertEqual(response.status_code, 301)    

    