import datetime as dt
from django.utils import timezone
from django.contrib.auth.models import User
from . import models as m


class Pomodoro():
    POMODORO_SEC = 25 * 60  # Pomodoro time                 [int, seconds]
    DELTA_SEC = 5 * 60  # Break time, after pomodoro    [int, seconds]

    def __init__(self):
        self.total_pomodoros = 0
        self.start_time = timezone.now()
        self.pomodoro_length = dt.timedelta(0, self.POMODORO_SEC)
        self.final_productive_time = self.start_time + self.pomodoro_length
        self.final_break_time = self.start_time + dt.timedelta(0,
                                                               self.POMODORO_SEC + self.DELTA_SEC)

        print(f"Bug check 0: \nt_now: {self.start_time}\nend_time: {self.final_productive_time}")

        print("Pomodoro Started!", "\nIt is now " + self.start_time.strftime("%H:%M") +
              " hrs. \nTimer set for 25 mins.")

    def run_timer(self):
        pomodoro = Pomodoro()

        # just for testing purposess
        counter = pomodoro.start_time.strftime("%H:%M:%S")
        user_name = "user" + counter
        user = User.objects.create_user(user_name, 'blabla@honey.com', 'winniepassword')
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
