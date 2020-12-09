"""View test example."""
# from django.test import TestCase
import os
from sys import platform
from timer import browserhistory
from unittest import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, Client

# class SessionModelTest(TestCase):

    # def test_start_button(self):
    #     c = Client()
    #     response = c.post('/', {'start_button_value': 'start'})
    #     print("STATUS IS " + str(response.status_code))
    #     self.assertEqual(response.status_code, 302)

class BrowserHistoryTestLinux(TestCase):
    def test_get_database_path(self):
        if platform == "linux" or platform == "linux2":
            linux_path = browserhistory.get_database_paths()['chrome']
            true_path = os.path.expanduser('~') + "/.config/google-chrome/Default/History"
            self.assertEqual(linux_path, true_path)

    def test_get_history(self):
        if platform == "linux" or platform == "linux2":
            history = browserhistory.get_browserhistory()['chrome']
            self.assertTrue(history)  #is false when i run it

class BrowserHistoryTestOSX(TestCase):
    def test_get_database_path(self):
        if platform == "darwin":
            osx_path = browserhistory.get_database_paths()['chrome']
            true_path = os.path.expanduser('~') + "/Library/Application Support/Google/Chrome/Default/History"
            self.assertEqual(osx_path, true_path)

    def test_get_history(self):
        if platform == "darwin":
            history = browserhistory.get_browserhistory()['chrome']
            self.assertTrue(history)  #is false when i run it

class BrowserHistoryTestWindows(TestCase):
    def test_get_database_path(self):
        if platform == "win32":
            win_path = browserhistory.get_database_paths()['chrome']
            true_path = os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
            self.assertEqual(win_path, true_path)

    def test_get_history(self):
        if platform == "win32":
            history = browserhistory.get_browserhistory()['chrome']
            self.assertTrue(history)  #is false when i run it