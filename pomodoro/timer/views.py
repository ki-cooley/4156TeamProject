from django.shortcuts import render
from django.http import HttpResponse
import requests as r
import sys
from subprocess import run, PIPE

# Create your views here.

def index(response):
    return HttpResponse ("<h1>Welcome to Pomodoro timer!</h1>")

def home(response):
    return render(response, "main/home.html", {})

def output(response):
    data=r.get("http://127.0.0.1:8800/")
    # print(data.text)
    data=data.text
    return render(response, "main/home.html")
    