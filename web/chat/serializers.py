from rest_framework import serializers
from .models import Chat, UserChat, Message


class ChatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'date', )


class ChatUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('jwt', 'user_id', )
