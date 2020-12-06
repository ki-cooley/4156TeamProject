from rest_framework import serializers
from .models import *


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDashboard
        fields = "__all__"

class TimerBlockedsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimerBlockedsite
        fields = "__all__"


class TimerSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimerSession
        fields = "__all__"


class TimerSessionactivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimerSessionactivity
        fields = "__all__"

