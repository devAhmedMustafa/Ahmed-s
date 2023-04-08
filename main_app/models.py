from django.db import models
from datetime import datetime

# Create your models here.

class Message(models.Model):

    content = models.TextField(null=True)
    date = models.DateField(default=datetime.now)

class SkillCategory(models.Model):

    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Skill(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/skills')
    perc = models.IntegerField()
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skill', null=True)

    def __str__(self):
        return self.name