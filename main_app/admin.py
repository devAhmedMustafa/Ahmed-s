from django.contrib import admin
from .models import Message, Skill, SkillCategory
# Register your models here.

admin.site.register(Message)
admin.site.register(Skill)
admin.site.register(SkillCategory)