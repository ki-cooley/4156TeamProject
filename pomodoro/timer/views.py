from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import pomodoro_timer as p
from django.contrib.auth.decorators import login_required


def index(response):
    return HttpResponse ("<h1>Welcome to Pomodoro timer!</h1>")

def home(response):
    return render(response, "timer/home.html", {})

@login_required
def start(response):
    if response.method == "POST":
        alldata = response.POST
        reset_button_value = alldata.get("reset_timer", 0)
        skip_value = alldata.get("skip_to_break", 0)
        if (str(reset_button_value) == "reset"):
            return redirect ('/start/')
        if (str(skip_value) == "skip_to_break"):
            return redirect ('/break/')
    else:
        alldata = response.POST
        usernamefield = alldata.get("username", 0)
        firstnamefield =alldata.get("firstname", 0)
        lastnamefield = alldata.get("lastname", 0)
        passwordfield = alldata.get("password1", 0)
        emailfield = alldata.get("email", 0)

        pomodoro = p.Pomodoro()
        pomodoro.run_timer()
        return render(response, "timer/start.html", {})

def start_break(response):
    if response.method == "POST":
        print("Hello from break()")
        alldata = response.POST
        reset_button_value = alldata.get("new_session", 0)
        print("new_session : " + str(reset_button_value))
        if (str(reset_button_value) == "new_session"):
            return redirect ('/start/')
    else:
        return render(response, "timer/break.html", {})

def output(response):
    if response.method == "POST":
        # parsing Http Response from UI start button 
        alldata = response.POST
        start_button_value = alldata.get("start_timer", 0)
        print("start_button_value : " + start_button_value)
        # call timer function
        return redirect('/start/')

    else: #GET method
        return render(response, "timer/home.html", {})

        
    