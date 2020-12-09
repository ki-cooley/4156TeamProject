from rest_framework import serializers
from .models import SessionActivity, BlockedSite, Session


class SessionActivitySerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = SessionActivity
        fields = ('site_url', 'visit_timestamp', 'user_id')
        #exclude = ['user_id']

    # def save(self):
    #     user_id = serializers.CurrentUserDefault()  # <= magic!
    #     title = self.validated_data['site_url']
    #     article = self.validated_data['visit_timestamp']

class BlockedSiteSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = BlockedSite
        fields = ('site_url', 'user_id')

class SessionSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Session
        fields = ('start_time', 'end_time', 'user_id')