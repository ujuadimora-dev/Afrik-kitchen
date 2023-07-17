from django.shortcuts import render
from .models import MenuItem

# Create your views here.


def food(request):
    menuitem = MenuItem.objects.all()
    context = {
        'menuitem': menuitem
    }
    return render(request, 'food/menu_list.html', context)


def detail(request, pk):
    menuitem = MenuItem.objects.get(pk=pk)
    return render(request, 'food/detail.html', {'menuitem': menuitem})
