from rest_framework import serializers
from .models import *


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDashboard
        fields = "__all__"