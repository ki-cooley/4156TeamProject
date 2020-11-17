from django.urls import path
from . import views, timer
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("<int:id>", views.index, name = "index"),
    path("", csrf_exempt(views.home), name="home"),
    path("timer", timer.run_timer, name="timer"),
    # path("", views.output, name="script"),
]
