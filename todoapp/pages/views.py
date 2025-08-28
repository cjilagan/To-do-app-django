from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request, *args, **kwargs):
    task = Task.objects.all()
    context = {'tasks': task, 'form': TaskForm()}

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid(): 
            form.save()
            context['form'] = TaskForm()
        return redirect('/')

    return render(request, 'home.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    context = {'form': form}
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'update.html', context)