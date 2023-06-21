from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.

def home(request):

    task=Task.objects.filter(is_completed=False)
    completedTask=Task.objects.filter(is_completed=True)
    context={
        'tasks':task,
        'completedTasks':completedTask
    }
    return render(request,'home.html',context)

def addTask(request):

    task=request.POST['addTask']
    print(task)
    Task.objects.create(task=task)
    
    return redirect('home')

def mark_as_done(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()

    return redirect('home')

def deleteTask(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')


def editTask(request,pk):
    task=get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        editedtask=request.POST['editTask']
        task.task=editedtask
        task.save()
        return redirect('home')
    else:
        taskvalue=task.task
    context={
        'tasks':task
    }
    return render(request,'edit.html',context)