from django.shortcuts import render
from django.http import HttpResponse
from .models import BreakFast, Lunch, Dinner, Sides
from django.conf import settings
from django.templatetags.static import static
import os


# Create your views here.


def index(request):
    ctx = {'name': 'Afrian Kitchen', 'msg': 'This is No 4 projects'}
    return render(request, 'menu/index.html', ctx) # menu here is the directory(path)


def menu(request):
    return render(request, 'menu/menu.html') # menu here is the directory(path)


def breakfast(request):
    path = settings.MEDIA_ROOT
    breakfasts = BreakFast.objects.all()
   
    ctx = {'breakfasts': breakfasts}
    print(breakfasts)
    return render(request, 'menu/breakfast.html', ctx)


def lunch(request):
    path = settings.MEDIA_ROOT
    lunchs = Lunch.objects.all()
   
    ctx = {'lunchs': lunchs}
    print(lunchs)
    return render(request, 'menu/lunch.html', ctx)


def dinner(request):
    path = settings.MEDIA_ROOT
    dinners = Dinner.objects.all()
   
    ctx = {'dinners': dinners}
    print(dinners)
    return render(request, 'menu/dinner.html', ctx)


def side(request):
    path = settings.MEDIA_ROOT
    sides = Side.objects.all()
   
    ctx = {'sides': sides}
    #print(sides)
    return render(request, 'menu/side.html', ctx)




