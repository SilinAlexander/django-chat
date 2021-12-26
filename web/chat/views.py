import logging

from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .services import ChatService
from . import serializers

logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


class ChatListView(ListAPIView):
    serializer_class = serializers.ChatListSerializer

    def get_queryset(self):
       return ChatService.user_chats(self.request.user.id)


class ChatUserView(ListAPIView):
    serializer_class = serializers.ChatUserSerializer

    # def get_queryset(self):
    #    return ChatService.
