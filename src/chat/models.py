from django.db import models
from uuid import uuid4


# Create your models here.
def generateUUID():
    return str(uuid4())

class Conversation(models.Model):
    conversation_id = models.CharField(max_length=255, unique=True, default=generateUUID, editable=False)
    def __str__(self):
        return "{}:{}..".format(self.id, self.conversation_id[:10])

class Message(models.Model):
    # Fields for messages
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    message_id = models.CharField(max_length=255, unique=True, default=generateUUID, editable=False)
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}:{}..".format(self.id, self.message_id[:10])