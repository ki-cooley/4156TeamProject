"""Pomodoro timer class."""
from django.utils import timezone as dt
import datetime
import pytz
from . import models as m


class Pomodoro:
    """Pomodoro class"""

    def __init__(self):
        pomodoro_sec = 25 * 60
        delta_sec = 5 * 60
        self.total_pomodoros = 0
        self.start_time = datetime.datetime.now(tz=pytz.timezone('US/Eastern')) - datetime.timedelta(hours=5)
        self.pomodoro_length = dt.timedelta(0, pomodoro_sec)
        self.final_productive_time = self.start_time + self.pomodoro_length
        self.final_break_time = self.start_time + dt.timedelta(0, pomodoro_sec + delta_sec)

    def run_timer(self, user):
        """Add to DB start and end time of pomodoro productive session."""
        # self.pomodoro = Pomodoro()
        self.start_time = datetime.datetime.now(tz=pytz.timezone('US/Eastern')) - datetime.timedelta(hours=5)

    def store(self, user):
        print('\n\nTimer ended!\n\n')
        end_time = datetime.datetime.now(tz=pytz.timezone('US/Eastern')) - datetime.timedelta(hours=5)
        entry = m.Session()
        entry.start_time = self.start_time
        entry.end_time = end_time
        entry.user_id = user
        entry.save()
