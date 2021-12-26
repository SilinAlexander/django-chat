from django.conf import settings

from .models import Chat, UserChat, Message


class ChatService:
    @staticmethod
    def user_chats(user_id: int):
        return Chat.objects.filter(user_chats__user=user_id)




