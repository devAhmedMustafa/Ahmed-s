from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_msg/', views.send_message, name='send_msg')
]
