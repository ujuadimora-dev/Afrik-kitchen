from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    ctx = {'name': 'Afrian Kitchen', 'msg': 'This is No 4 projects'}
    return render(request, 'menu/index.html', ctx) # menu here is the directory(path)


def menu(request):
    return render(request, 'menu/menu.html') # menu here is the directory(path)
