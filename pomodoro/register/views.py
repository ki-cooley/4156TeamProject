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
            return redirect("/account/login/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})


def logout_page(response):
    response.session.clear()
    # response.delete_cookie(key='username')
    return render(response, "registration/logout.html", {})
    # return render_to_response(response, "registration/logout.html", {})


def github_user(access_token):
    """
    通过传入的access_token，带上access_token参数，向GitHub用户API发送请求以获取用户信息；
    :param access_token: 用于访问API的token
    :return: 成功返回用户信息，失败返回None
    """
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
    """
    通过传入的 code 参数，带上client_id、client_secret、和code请求GitHub，以获取access_token
    :param code: 重定向获取到的code参数
    :return: 成功返回acces_token；失败返回None；
    """
    token_url = 'https://github.com/login/oauth/access_token?' \
                'client_id={}&client_secret={}&code={}'
    token_url = token_url.format(SOCIAL_AUTH_GITHUB_KEY, SOCIAL_AUTH_GITHUB_SECRET,
                                 code)  # 这里的client_id、client_secret修改为自己的真实ID与Secret
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
                if not User.objects.all().filter(username=name).exists():
                    User.objects.create_user(username=name, password='', email=email)
                user_obj = auth.authenticate(username=name, password='')
                auth.login(request, user_obj)
                return redirect('/')
        return HttpResponse('failed to get the parameter of token, please retry!')
    return HttpResponse('failed to get the parameter of CODE, please retry!')
