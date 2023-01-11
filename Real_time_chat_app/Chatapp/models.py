from django.db import models
from datetime import datetime


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name

class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    