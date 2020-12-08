from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "firstname", "lastname", "email", "password1", "password2"]


class GithubRegisterForm(UserCreationForm):
    social_auth = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ["username", "firstname", "lastname", "social_auth", "email", "password1", "password2"]
