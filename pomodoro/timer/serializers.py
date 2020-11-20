from rest_framework import serializers
from .models import SessionActivity


class SessionActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionActivity
        fields = ('site_url', 'visit_timestamp', 'user_id')
