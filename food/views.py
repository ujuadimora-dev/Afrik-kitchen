from django.shortcuts import render, redirect, get_object_or_404
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

def manage_menu(request):
    menuitems = MenuItem.objects.all()
    context = {
        'menuitems': menuitems
    }
    return render(request, 'food/manage_menu.html', context)


def delete_menuitem(request, pk):
    menuitem = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        menuitem.delete()
        return redirect('food:food')  # Redirect to menu_list view
    return render(request, 'food/delete_menuitem.html', {'menuitem': menuitem})


def update_menuitem(request, pk):
    menuitem = get_object_or_404(MenuItem, pk=pk)
    form = MenuitemDetail(request.POST or None, instance=menuitem)
    if form.is_valid():
        form.save()
        return redirect('food:food')  # Redirect to menu_list view
    return render(request, 'food/update_menu.html', {'form': form})

