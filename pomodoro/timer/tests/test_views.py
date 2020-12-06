"""View test example."""
from django.test import TestCase
import pytest

from unittest import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse, resolve
from mixer.backend.django import mixer
from timer import views as v


@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        mixer.blend('timer.Session')
        cls.factory = RequestFactory()

    def test_home_authenticated(self):
        path = reverse('home', kwargs={})
        request = self.factory.get(path)
        request.user = mixer.blend(User)
        response = v.home(request)
        assert response.status_code == 200

    def test_start_nonauthenticated(self):
        path = reverse('start', kwargs={})
        request = self.factory.get(path)

        request.user = AnonymousUser()
        response = v.start(request)
        assert response.status_code == 200
        # assert 'accounts/login' in response.url

    def test_start_nonauthenticated(self):
        path = reverse('home', kwargs={})
        request = self.factory.get(path)
        request.user = AnonymousUser()
        response = v.home(request)
        assert response.status_code == 200

    def test_break_nonauthenticated(self):
          path = reverse('break', kwargs={})
          request = self.factory.get(path)
          request.user = AnonymousUser()
          response = v.start_break(request)
          assert response.status_code == 200

    def test_break_nonauthenticated(self):
        path = reverse('break', kwargs={})
        request = self.factory.get(path)
        request.user = AnonymousUser()
        response = v.start_break(request)
        assert response.status_code == 200