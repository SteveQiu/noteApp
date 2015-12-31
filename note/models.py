from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    uid = models.CharField(max_length=20)
    pwd = models.CharField(max_length=32)
    email = models.CharField(max_length=40)
