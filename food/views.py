from django.shortcuts import render, redirect
from .models import MenuItem
from .forms import MenuitemDetail


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


def create_menuitem(request):
        form = MenuitemDetail(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('food:food')  # Redirect to menu_list view
    
        return render(request, 'food/create_menu.html', {'form': form})
