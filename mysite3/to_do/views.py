from django.shortcuts import render
from .models import Task

def index(request):
    num_task = Task.objects.count()
   
    context = {
        "num_task" : num_task,
    }
    return render(request, 'base.html', context=context)