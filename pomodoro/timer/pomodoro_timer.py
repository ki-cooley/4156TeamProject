"""Pomodoro timer class."""
import datetime as dt

from django.contrib.auth.models import User
from django.utils import timezone

from . import models as m


class Pomodoro:
    """Pomodoro class"""

    def __init__(self):
        pomodoro_sec = 25 * 60
        delta_sec = 5 * 60
        self.total_pomodoros = 0
        self.start_time = timezone.now()
        self.pomodoro_length = dt.timedelta(0, pomodoro_sec)
        self.final_productive_time = self.start_time + self.pomodoro_length
        self.final_break_time = self.start_time + dt.timedelta(0,
                                                               pomodoro_sec + delta_sec)

    @staticmethod
    def run_timer():
        """Add to DB start and end time of pomodoro productive session."""
        pomodoro = Pomodoro()

        # just for testing purposes
        counter = pomodoro.start_time.strftime("%H:%M:%S")
        user_name = "user" + counter
        user = User.objects.create_user(user_name, 'blabla@honey.com', 'password')
        user.last_name = 'holmes'
        print('\n\nTimer started!\n\n')
        ####

        entry = m.Session()
        db_start_time = pomodoro.start_time
        db_end_time = pomodoro.final_productive_time

        print("db_start_time " + db_start_time.strftime("%H:%M"))
        print("db_end_time " + db_end_time.strftime("%H:%M"))

        entry.start_time = db_start_time
        entry.end_time = db_end_time
        entry.user_id = user
        entry.save()