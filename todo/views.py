from django.shortcuts import render
from .models import Task
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def add_task(request):
    task = request.POST['task']
    # since we are importing our models we can implement them in our objects.create method
    # our models are the following: task, is_completed, created_at, updated_at
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    # After marking the task as done, we can redirect to the home page or return a
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed= False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task # updating the task
        get_task.save()
        return redirect('home')
    # If the request method is GET, we will render the edit task page with the current task details
    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')