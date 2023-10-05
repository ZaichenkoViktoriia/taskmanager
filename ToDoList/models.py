from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class Manager(AbstractUser):
    def __str__(self):
        return self.username


class Task(models.Model):
    name = models.CharField(max_length=63, default=None)
    content = models.TextField(default=None)
    created_date = models.DateTimeField(default=datetime.now)
    tag = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self):
        return f"{self.name} {self.content} {self.created_date} {self.tag}"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
