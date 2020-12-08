"""Views for timer."""
from django.shortcuts import render, redirect
from . import pomodoro_timer as p
from django.contrib.auth.decorators import login_required

from rest_framework import status, viewsets
from .serializers import SessionActivitySerializer, BlockedSiteSerializer, SessionSerializer
from .models import SessionActivity, BlockedSite, Session
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SessionActivityViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    permission_classes = (IsAuthenticated,)
    queryset = SessionActivity.objects.all().order_by('user_id')
    serializer_class = SessionActivitySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BlockedSiteViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)
    #queryset = BlockedSite.objects.all().order_by('user_id')
    serializer_class = BlockedSiteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #change to return sites of only currently authenticated user later
    def get_queryset(self):
        user_id = self.request.user.id
        return BlockedSite.objects.filter(user_id=user_id)

class SessionViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    permission_classes = (IsAuthenticated,)
    #queryset = BlockedSite.objects.all().order_by('user_id')
    serializer_class = SessionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #change to return sites of only currently authenticated user later
    def get_queryset(self):
        user_id = self.request.user.id
        return Session.objects.filter(user_id=user_id)

def start(response):
    """start view."""
    if response.method == "POST":
        alldata = response.POST
        reset_button_value = alldata.get("reset_timer", 0)
        skip_value = alldata.get("skip_to_break", 0)

        if str(reset_button_value) == "reset":
            return redirect('/start/')
        if str(skip_value) == "skip_to_break":
            current_user = response.user
            pomodoro = p.Pomodoro()
            pomodoro.run_timer(current_user)
            return redirect('/break/')
    else:
        current_user = response.user
        pomodoro = p.Pomodoro()
        pomodoro.run_timer(current_user)
        return render(response, "timer/start.html", {})


def start_break(response):
    """start break endpoint."""
    if response.method == "POST":
        print("Hello from break()")
        alldata = response.POST
        reset_button_value = alldata.get("new_session", 0)
        print("new_session : " + str(reset_button_value))
        if str(reset_button_value) == "new_session":
            current_user = response.user
            pomodoro = p.Pomodoro()
            pomodoro.run_timer(current_user)
            return redirect('/start/')
    else:
        return render(response, "timer/break.html", {})


def home(response):
    """start endpoint."""
    if response.user.is_authenticated:

        current_user = response.user
        print( current_user.id)
        print("USER ID ")
        if response.method == "POST":
            alldata = response.POST
            if alldata.get("start_timer", 0) == "dashboard":
                return redirect("/dashboard/session/" + str(response.user.id) +"/all")
            start_button_value = alldata.get("start_timer", 0)
            print("start_button_value : " + str(start_button_value))
            # call timer function
            return redirect('/start/')
        return render(response, "timer/home.html", {})
    else:
        if response.method == "POST":
            return redirect('/account/login/')
        return render(response, "timer/home.html", {})
