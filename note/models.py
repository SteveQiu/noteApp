from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    uid = models.CharField(max_length=20)
    pwd = models.CharField(max_length=32)
    email = models.CharField(max_length=40)

class Note(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=400)
