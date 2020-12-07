"""pomodoro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from register import views as vregister
from django.views.decorators.csrf import csrf_exempt

urlpatterns = (
    path('admin/', admin.site.urls),
    path('register/', vregister.register, name="register"),
    path('', include("timer.urls")),
    path('account/', include("django.contrib.auth.urls")),
    path('logout_page/', vregister.logout_page, name="logout"),
    path('login/github/', include('social_django.urls', namespace='social')),
    path('github/redirect/', vregister.github_redirect, name='github_redirect'),

    # path('login/github/', include('social_django.urls', namespace='social')),
    # path('google_oauth/redirect/', vregister.CallbackView, name="google_callback"),
)



