from django.shortcuts import render

from .models import Task
# Create your views here.
def index(request, *args, **kwargs):
    task = Task.objects.all()
    context = {'tasks': task}

    return render(request, 'home.html', context)