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
