from django.shortcuts import render
from .models import Message
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