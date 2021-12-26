import pytz
from rest_framework import serializers


class SetTimeZoneSerializer(serializers.Serializer):
    timezone = serializers.ChoiceField(choices=pytz.common_timezones)


class LoginServiceSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()



