from django.shortcuts import render, redirect
from .models import Post, Task, Reader
from .forms import ReaderForm


def index(request):

    posts = Post.objects.all()
    tasks = Task.objects.all()

    return render(request, 'main/index.html', {'title': 'POPS', 'posts': posts, 'tasks': tasks})


def content(request):
    return render(request, 'main/content.html')


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chitka')
        else:
            error = 'Некорректные данные'

    form = ReaderForm()
    data = {
        'form': form,
        'error': error
        }
    return render(request, 'main/create.html', data)

def chitka(request):
    readers = Reader.objects.all()
    return render(request, 'main/chitka1.html', {'readers': readers})

def chitka2(request):
    readers = Reader.objects.all()
    return render(request, 'main/chitka2.html', {'readers': readers})

def chitka3(request):
    readers = Reader.objects.all()
    return render(request, 'main/chitka3.html', {'readers': readers})

def log_in(request):
    return render(request, 'main/login.html')

def sign_up(request):
    return render(request, 'main/signup.html')
