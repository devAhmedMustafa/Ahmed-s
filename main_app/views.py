from django.shortcuts import render
from .models import Message, Skill, SkillCategory
from django.http import JsonResponse
import json

# Create your views here.

def home(request):

    return render(request, 'home.html', {})

def send_message(request):
   
    message = request.GET['message']
    
    x = Message(content=message)
    x.save()

    data = {
        'message':message
    }

    return JsonResponse(data)

def skills(request):

    categories = SkillCategory.objects.all()
    skills = Skill.objects.all()

    return render(request, 'skills.html', {'categories': categories, 'skills':skills})

def projects(request):

    return render(request, 'projects.html', {})