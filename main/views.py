from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'главная стр сайта', 'tasks': tasks})



def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'


    form = TaskForm()
    context = {
        'form': form,
        "error": error
    }
    return render(request, 'main/create.html', context)


def FAQs(request):
    return render(request, 'main/FAQs.html')

