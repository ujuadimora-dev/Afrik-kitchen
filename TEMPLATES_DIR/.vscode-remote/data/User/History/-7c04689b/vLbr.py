from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    ctx = {'name': 'Afrian Kitchen'}
    return render(request, 'menu/index.html', ctx)


def menu(request):
    return HttpResponse('view the menu list here')
