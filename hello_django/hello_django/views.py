from django.http import HttpResponse
from django.shortcuts import render

def about(recuest):
    return render(recuest, 'about.html',{'greeting':'Hello'})

def home(recuest):
    return HttpResponse('This is my home')