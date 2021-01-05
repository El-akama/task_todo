from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


def index(request):
    task = Todo.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'task/list.html', {
        'task': task,
        'form': form,
        })

def update_task(request, pk):
    task = Todo.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method =='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'task/update.html', {'form': form})


def delete_task(request, pk):
    item = Todo.objects.get(id=pk)

    if request.method =='POST':
        item.delete()
        return redirect('/')
        
    return render(request, 'task/delete.html', {'item': item})