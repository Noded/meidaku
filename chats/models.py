from django.contrib.auth import get_user_model
from django.db import models
from uuid import uuid4

# Create your models here.

User = get_user_model()


class Group(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    members = models.ManyToManyField(User, related_name='user_groups', blank=True)

    def add_user(self, user):
        if not self.members.filter(pk=user.pk).exists():
            self.members.add(user)
        return

    def remove_user(self, user):
        if self.members.filter(pk=user.pk).exists():
            self.members.remove(user)
        return


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
