from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BreakFast, Lunch, Dinner, Sides
from django.conf import settings
from django.templatetags.static import static
from .forms import MenuCreateForm
from view_menu.forms import MenuForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotFound

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
    sides = Sides.objects.all()
   
    ctx = {'sides': sides}
    print(sides)
    return render(request, 'menu/side.html', ctx)


"""" for the creating the menu"""


def create_menu(request):
    if request.method == 'POST':
        form = MenuCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            menu_type = form.cleaned_data['menu_type']
            
            if menu_type == 'BREAKFAST':
                # Save data to Breakfast model
                breakfast = BreakFast.objects.create(
                    description=form.cleaned_data['description'],
                    #content=form.cleaned_data['content'],
                    fimage=form.cleaned_data['fimage'],
                    name=form.cleaned_data['name'],
                    priceM=form.cleaned_data['priceM'],
                    priceL=form.cleaned_data['priceL'],
                    vegetarian=form.cleaned_data['vegetarian'],
                    calorie_count=form.cleaned_data['calorie_count']
                )
                
                
                #return render(request, 'menu/success.html')
                return render(request, 'menu/success.html', {'menu_type': 'breakfast'})
                
            elif menu_type == 'LUNCH':
                # Save data to Lunch model
                lunch = Lunch.objects.create(
                    description=form.cleaned_data['description'],
                    #content=form.cleaned_data['content'],
                    fimage=form.cleaned_data['fimage'],
                    name=form.cleaned_data['name'],
                    priceM=form.cleaned_data['priceM'],
                    priceL=form.cleaned_data['priceL'],
                    vegetarian=form.cleaned_data['vegetarian'],
                    calorie_count=form.cleaned_data['calorie_count']
                )
                
                
               # return render(request, 'menu/success.html')
                return render(request, 'menu/success.html', {'menu_type': 'lunch'})
                
            elif menu_type == 'DINNER':
                # Save data to Dinner model
                dinner = Dinner.objects.create(
                   
                    #content=form.cleaned_data['content'],
                    description=form.cleaned_data['description'],
                    fimage=form.cleaned_data['fimage'],
                    name=form.cleaned_data['name'],
                    priceM=form.cleaned_data['priceM'],
                    priceL=form.cleaned_data['priceL'],
                    vegetarian=form.cleaned_data['vegetarian'],
                    calorie_count=form.cleaned_data['calorie_count']
                )
               
                
                return render(request, 'menu/success.html')
                return render(request, 'menu/success.html', {'menu_type': 'dinner'})
                
            elif menu_type == 'SIDE':
                # Save data to Sides model
                sides = Sides.objects.create(
                    description=form.cleaned_data['description'],
                    #content=form.cleaned_data['content'],
                    fimage=form.cleaned_data['fimage'],
                    name=form.cleaned_data['name'],
                    priceM=form.cleaned_data['priceM'],
                    priceL=form.cleaned_data['priceL'],
                    vegetarian=form.cleaned_data['vegetarian'],
                    calorie_count=form.cleaned_data['calorie_count']
                )
             
                
                return render(request, 'menu/success.html')
                return render(request, 'menu/success.html', {'menu_type': 'side'})
    else:
        form = MenuCreateForm()

    context = {'form': form}
    return render(request, 'menu/create_menu.html', context)

#  