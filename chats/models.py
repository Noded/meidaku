from django.contrib.auth import get_user_model
from django.db import models
from uuid import uuid4

# Create your models here.

User = get_user_model()


class Group(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    members = models.ManyToManyField(User, related_name='user_groups', blank=True)
    name = models.CharField(max_length=24)
    
    def __str__(self):
        return self.name

    def add_user(self, user):
        self.members.add(user)

    def remove_user(self, user):
        self.members.remove(user)
        
class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message by {self.author} at {self.timestamp}"

