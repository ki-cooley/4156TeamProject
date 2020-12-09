#from unittest import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, Client
from timer.api_local import login, get_blocked_sites, send_blocked_sites
from rest_framework.authtoken.models import Token


class RemoteLoginTest(TestCase):

    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='12345')
        user.save()

    def test_valid_login(self):
        #print(self.user)
        response_token = login(username='testuser', password='12345')
        self.assertEqual(True, response_token)

    def test_wrong_pass(self):
        #self.user = User.objects.create_user(username='testuser', password='12345')
        response_token = login(username='testuser', password='1234')
        self.assertEqual(None, response_token)

    def test_no_user(self):
        #self.user = User.objects.create_user(username='testuser', password='12345')
        response_token = login(username='usertest', password='1234')
        self.assertEqual(False, response_token)

