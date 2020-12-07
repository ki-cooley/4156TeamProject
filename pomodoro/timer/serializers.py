from rest_framework import serializers
from .models import SessionActivity, BlockedSite


class SessionActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionActivity
        fields = ('site_url', 'visit_timestamp', 'user_id')

class BlockedSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedSite
        fields = ('site_url', 'user_id')