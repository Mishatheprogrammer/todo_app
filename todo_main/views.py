from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks123': tasks
    }
    return render(request, 'home.html', context)