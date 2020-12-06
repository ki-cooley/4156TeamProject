from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt
import os
import google_apis_oauth

from django.shortcuts import HttpResponseRedirect

# The url where the google oauth should redirect
# after a successful login.
REDIRECT_URI = 'http://127.0.0.1:8000/google_oauth/callback/'

# Authorization scopes required
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/userinfo.email',
          'https://www.googleapis.com/auth/userinfo.profile',
          'https://www.googleapis.com/auth/gmail.insert']

# Path of the "client_id.json" file
JSON_FILEPATH = os.path.join(os.getcwd(), 'client_secret.json')


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
    return render(response, "registration/logout.html", {})
    # return render_to_response(response, "registration/logout.html", {})

def RedirectOauthView(response):
    oauth_url = google_apis_oauth.get_authorization_url(
        JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return HttpResponseRedirect(oauth_url)

