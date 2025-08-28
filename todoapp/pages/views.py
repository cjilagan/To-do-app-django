from django.shortcuts import render

from .models import *
from .forms import *
# Create your views here.
def index(request, *args, **kwargs):
    task = Task.objects.all()
    context = {'tasks': task, 'form': forms}

    return render(request, 'home.html', context)