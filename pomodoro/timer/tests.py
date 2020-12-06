"""View test example."""
# from django.test import TestCase
import os
from . import browserhistory
from unittest import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, Client

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
#
class BrowserHistoryTestLinux(TestCase):
    def test_get_database_path(self):
        linux_path = browserhistory.get_database_paths()['chrome']
        true_path = os.path.expanduser('~') + "/.config/google-chrome/Default/History"
        self.assertEqual(linux_path, true_path)

    def test_get_history(self):
        history = browserhistory.get_browserhistory()['chrome']
        self.assertTrue(history)  #is false when i run it

