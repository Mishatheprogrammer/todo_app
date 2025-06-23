from django.shortcuts import render
from .models import Task
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def add_task(request):
    task = request.POST['task']
    # since we are importing our models we can implement them in our objects.create method
    # our models are the following: task, is_completed, created_at, updated_at
    Task.objects.create(task=task)
    return redirect('home')