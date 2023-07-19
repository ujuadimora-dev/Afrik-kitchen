from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return request('<h1>hellow World </h1> <h2 style=" style":color:red> Home page</h2>')


def menu(request):
    return HttpResponse('view the menu list here' )
