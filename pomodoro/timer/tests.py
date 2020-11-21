"""View test example."""
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, Client
from . import views as v
from . import models as m
from django.utils import timezone


class SessionModelTest(TestCase):

    def test_start_button(self):
        c = Client()
        response = c.post('/', {'start_button_value': 'start'})
        print("STATUS IS " + str(response.status_code))
        self.assertEqual(response.status_code, 302)

    def test_home(self):
        c = Client()
        response = c.get('/')
        print("STATUS IS " + str(response.status_code))
        self.assertEqual(response.status_code, 200)

    def test_start2(self):
        c = Client()
        response = c.get('/start/', {'start_button_value': 'start'})
        self.assertEqual(response.status_code, 200)

    def test_break(self):
        c = Client()
        response = c.get('/break/')
        self.assertEqual(response.status_code, 200)
