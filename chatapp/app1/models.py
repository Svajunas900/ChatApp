from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Conversation(models.Model):
  name = models.CharField(max_length=30)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name}"


class Messages(models.Model):
  conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  user_name = models.CharField(max_length=100)
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  

  def __str__(self):
    return f"{self.user_name}: {self.text}"