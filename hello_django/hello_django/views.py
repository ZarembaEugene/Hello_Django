from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a = 6+5
    return render(request, 'about.html', {'greetings': a})

def home(request):
    return HttpResponse('This is my home page')
