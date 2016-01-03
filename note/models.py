from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Note(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=400)
