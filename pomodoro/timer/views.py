"""Views for timer."""
from django.shortcuts import render, redirect
from . import pomodoro_timer as p


def start(response):
    """start view."""
    if response.method == "POST":
        alldata = response.POST
        reset_button_value = alldata.get("reset_timer", 0)
        skip_value = alldata.get("skip_to_break", 0)
        if str(reset_button_value) == "reset":
            return redirect('/start/')
        if str(skip_value) == "skip_to_break":
            return redirect('/break/')
    else:
        pomodoro = p.Pomodoro()
        pomodoro.run_timer()
        return render(response, "timer/start.html", {})


def start_break(response):
    """start break endpoint."""
    if response.method == "POST":
        print("Hello from break()")
        alldata = response.POST
        reset_button_value = alldata.get("new_session", 0)
        print("new_session : " + str(reset_button_value))
        if str(reset_button_value) == "new_session":
            return redirect('/start/')
    else:
        return render(response, "timer/break.html", {})


def home(response):
    """start endpoint."""
    if response.method == "POST":
        alldata = response.POST
        start_button_value = alldata.get("start_timer", 0)
        print("start_button_value : " + str(start_button_value))
        # call timer function
        return redirect('/start/')
    return render(response, "timer/home.html", {})
