from django.db import models
from uuid import uuid4


def hex_uuid():
    return uuid4().hex


class Chat(models.Model):
    id = models.CharField(max_length=32, primary_key=True, editable=False, default=hex_uuid, db_index=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']


class Message(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.PositiveIntegerField(db_index=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        ordering = ['-date']


class UserChat(models.Model):
    user = models.PositiveIntegerField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='user_chats')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'chat'], name='unique_user_in_chat')
        ]
