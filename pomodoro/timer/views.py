from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse ("<h1>Welcome to Pomodoro timer!</h1>")

def v1(response):
    return HttpResponse ("<h1>This is v1!</h1>")