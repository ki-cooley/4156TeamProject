import time
import datetime as dt

import tkinter
from tkinter import messagebox
from tkinter import simpledialog
from . import models as m
from django.contrib.auth.models import User


class Pomodoro():
    POMODORO_SEC = 25 * 60  # Pomodoro time                 [int, seconds]
    DELTA_SEC = 5 * 60  # Break time, after pomodoro    [int, seconds]

    def __init__(self):
        self.total_pomodoros = 0
        self.start_time = dt.datetime.now()  # Current time for reference.   [datetime object]
        self.pomodoro_length = dt.timedelta(0, self.POMODORO_SEC)  # Time delta in mins            [datetime object]
        self.final_productive_time = self.start_time + self.pomodoro_length  # Future time for reference     [datetime object]
        self.final_break_time = self.start_time + dt.timedelta(0,
                                                               self.POMODORO_SEC + self.DELTA_SEC)  # Final time (w/ 5 mins break)  [datetime object]

        print(f"Bug check 0: \nt_now: {self.start_time}\nend_time: {self.final_productive_time}")

        print("Pomodoro Started!", "\nIt is now " + self.start_time.strftime("%H:%M") +
              " hrs. \nTimer set for 25 mins.")

    def start_new_timer(self):
        '''
            Resets time variables for a new pomodoro.
        '''

        self.start_time = dt.datetime.now()
        self.final_productive_time = self.start_time + dt.timedelta(0, self.POMODORO_SEC)
        self.final_break_time = self.start_time + dt.timedelta(0, self.POMODORO_SEC + self.DELTA_SEC)
        print('\n---- Began new pomodoro! ----\n')

    def run_timer(self, response):
        pomodoro = Pomodoro()
        # just for testing purposess
        counter = pomodoro.start_time.strftime("%H:%M:%S")
        user_name = response.user.firstname + counter
        user = User.objects.create_user(user_name, response.user.get('email'), response.user.get('password1'))
        user.last_name = response.user.get('lastname')
        print('\n\nTimer started!\n\n')

        final_productive_time = pomodoro.final_productive_time
        entry = response.user.session
        db_start_date = pomodoro.start_time.date()
        db_start_time = pomodoro.start_time.time()
        db_end_date = pomodoro.final_break_time.date()
        db_end_time = pomodoro.final_break_time.time()

        print("db_start_date " + db_start_date.strftime("%H:%M"))
        print("db_start_time " + db_start_time.strftime("%H:%M"))
        print("db_end_date " + db_end_date.strftime("%H:%M"))
        print("db_end_time " + db_end_time.strftime("%H:%M"))

        entry.start_day = db_start_date
        entry.start_time = db_start_time
        entry.end_day = db_end_date
        entry.end_time = db_end_time
        entry.user_id = user
        entry.save()