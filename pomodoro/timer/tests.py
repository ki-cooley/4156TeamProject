# from django.test import TestCase
import os
from timer import browserhistory
from unittest import TestCase

class BrowserHistoryTestLinux(TestCase):
    def test_get_database_path(self):
        linux_path = browserhistory.get_database_paths()['chrome']
        true_path = os.path.expanduser('~') + "/.config/google-chrome/Default/History"
        self.assertEqual(linux_path, true_path)

    def test_get_history(self):
        history = browserhistory.get_browserhistory()['chrome']
        self.assertTrue(history)
