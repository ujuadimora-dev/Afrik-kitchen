from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem
from .forms import MenuitemDetail
from django.contrib import messages
from django.http import HttpResponse


def food(request):
    """ view the menu list"""
    menuitem = MenuItem.objects.all()
    context = {
        'menuitem': menuitem
    }
    return render(request, 'food/menu_list.html', context)


def detail(request, pk):
    """ view the details of the menu"""
    menuitem = MenuItem.objects.get(pk=pk)
    return render(request, 'food/detail.html', {'menuitem': menuitem})


def create_menuitem(request):
    """ To create the menu item"""
    form = MenuitemDetail(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Menu item created successfully.')
        return redirect('food:food')  # Redirect to menu_list view
        return render(request, 'food/create_menu.html', {'form': form})


def manage_menu(request):
    """To manage menu """
    menuitems = MenuItem.objects.all()
    context = {
        'menuitems': menuitems
    }
    return render(request, 'food/manage_menu.html', context)


def delete_menuitem(request, pk):
    """ To delete menu item"""
    menuitem = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        menuitem.delete()
        messages.success(request, 'Menu item deleted successfully.')
        return redirect('food:food')  # Redirect to menu_list view
    return render(request, 'food/delete_menuitem.html', {'menuitem': menuitem})


def update_menuitem(request, pk):
    """ To update the menu item """
    menuitem = get_object_or_404(MenuItem, pk=pk)
    form = MenuitemDetail(request.POST or None, instance=menuitem)
    if form.is_valid():
        form.save()
        messages.success(request, 'Menu item updated successfully.')
        return redirect('food:food')  # Redirect to menu_list view
    return render(request, 'food/update_menu.html', {'form': form})


