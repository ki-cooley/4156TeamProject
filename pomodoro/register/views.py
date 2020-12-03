from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt


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
    return render(response, "registration/logout.html", {})
    # return render_to_response(response, "registration/logout.html", {})

