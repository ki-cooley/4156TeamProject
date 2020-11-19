from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests as r
import sys
from subprocess import run, PIPE
from django.views.generic import TemplateView
from . import pomodoro_timer as p


def index(response):
    return HttpResponse("<h1>Welcome to Pomodoro timer!</h1>")

def home(response):
    return render(response, "timer/home.html", {})

def start(response):
    if response.method == "POST":
        print("Hello from start()")
        alldata = response.POST
        reset_button_value = alldata.get("reset_timer", 0)
        print("reset_button_value : " + str(reset_button_value))
        return redirect('/start')

    else:
        pomodoro = p.Pomodoro()
        pomodoro.run_timer()
        return render(response, "timer/start.html", {})

def output(response):
    print(response.method)

    if response.method == "POST":
        print("******")
        print(response.POST)
        print("******")

        # parsing Http Response from UI start button
        alldata = response.POST
        start_button_value = alldata.get("start_timer", 0)
        print("start_button_value : " + start_button_value)
        # call timer function
        return redirect('/start/')

    else:  # GET method
        # redirect('start/', "timer/home.html", {})
        return render(response, "timer/home.html", {})
        # do



