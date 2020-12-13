import json
import time
import urllib

import google_auth_oauthlib
import requests
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from httplib2 import Http

from pomodoro.settings import SOCIAL_AUTH_GITHUB_KEY, SOCIAL_AUTH_GITHUB_SECRET
from .forms import RegisterForm, GithubRegisterForm
from django.views.decorators.csrf import csrf_exempt
import os


# Create your views here.
@csrf_exempt
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            # return redirect("/account/login/")
            return render(response, "registration/login.html", {})
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})


def logout_page(response):
    response.session.clear()
    # response.delete_cookie(key='username')
    return render(response, "registration/logout.html", {})
    # return render_to_response(response, "registration/logout.html", {})


def github_user(access_token):
    user_url = 'https://api.github.com/user'
    access_token = 'token {}'.format(access_token)
    headers = {
        'accept': 'application/json',
        'Authorization': access_token
    }
    res = requests.get(user_url, headers=headers)
    print(res.content)
    if res.status_code == 200:
        user_info = res.json()
        print(user_info)
        return user_info
    return 400


def github_token(code):
    token_url = 'https://github.com/login/oauth/access_token?' \
                'client_id={}&client_secret={}&code={}'
    token_url = token_url.format(SOCIAL_AUTH_GITHUB_KEY, SOCIAL_AUTH_GITHUB_SECRET,
                                 code)
    header = {
        'accept': 'application/json'
    }
    res = requests.post(token_url, headers=header)
    # print(">>>>>>>>>>>>>>>>>>")
    # print(res.status_code)
    # print(">>>>>>>>>>>>>>>>>>")and res.json()['error'] is None
    if res.status_code == 200 :
        res_dict = res.json()
        print(res_dict)
        print(type(res_dict))
        return res_dict['access_token']
    return 400


def github_redirect(request):
    req_info = request.GET
    req_code = req_info.get('code', None)
    if req_code:
        access_token = github_token(req_code)
        if access_token:
            user_info = github_user(access_token)
            if user_info:
                user_name = user_info.get('login', None)
                name = user_info.get('name', None)
                email = user_info.get('email', None)
                social_auth = user_info.get('id', None)
                if not User.objects.all().filter(username=user_name, first_name=name.split(' ', 1)[0],
                                                 last_name=name.split(' ', 1)[1]).exists():
                    User.objects.create_user(username=user_name, password='', email=email,
                                             first_name=name.split(' ', 1)[0], last_name=name.split(' ', 1)[1])
                user_obj = auth.authenticate(request, username=user_name, password='')
                auth.login(request, user_obj)
                return redirect('/')
        return HttpResponse('failed to get the parameter of token, please retry!')
    return HttpResponse('failed to get the parameter of CODE, please retry!')
