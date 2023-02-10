from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskCreateUpdateForm

def index(request):
    num_task = Task.objects.count()
   
    context = {
        "num_task" : num_task,
    }
    return render(request, 'index.html', context=context)

@login_required
def view_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})

# @login_required
# def create_task(request):
#     if request.method == 'POST':
#         task = Task(text=request.POST['Text'], user=request.user)
#         task.save()
#         return redirect('view_tasks')
#     return render(request, 'create_task.html')
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskCreateUpdateForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('tasks')
    else:
        form = TaskCreateUpdateForm()
    return render(request, 'create_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.text = request.POST['text']
        task.save()
        return redirect('view_tasks')
    return render(request, 'edit_task.html', {'task': task})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('view_tasks')