from django.db import models
from datetime import datetime

# Create your models here.

class Message(models.Model):
    content = models.TextField(null=True)
    date = models.DateField(default=datetime.now)