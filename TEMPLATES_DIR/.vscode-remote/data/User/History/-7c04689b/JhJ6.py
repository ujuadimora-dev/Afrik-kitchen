from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'view_menu/index.html')


def menu(request):
    return HttpResponse('view the menu list here' )
