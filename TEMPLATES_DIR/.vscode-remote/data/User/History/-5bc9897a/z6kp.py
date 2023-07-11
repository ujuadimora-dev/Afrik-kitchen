from django.shortcuts import render
from django.http import HttpResponse
from .models import BreakFast, Lunch, Dinner, Sides
from django.conf import settings
from django.templatetags.static import static
from .forms import MenuCreateForm
from view_menu.forms import MenuForm

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
            # Get the menu type and menu details from the form data
            menu_type = form.cleaned_data['menu_type']
            menu_details = form.cleaned_data['menu_details']
            
            # Save the data to the respective models (Breakfast, Lunch, Dinner, Sides)
            if menu_type == 'BREAKFAST':
                breakfast = Breakfast.objects.create(
                    name=menu_details['name'],
                    priceM=menu_details['priceM'],
                    priceL=menu_details['priceL'],
                    fimage=menu_details['image'],
                    description=menu_details['content'],
                )
                # Additional processing if needed
                
            elif menu_type == 'LUNCH':
                lunch = Lunch.objects.create(
                    name=menu_details['name'],
                    priceM=menu_details['priceM'],
                    priceL=menu_details['priceL'],
                    fimage=menu_details['image'],
                )
                # Additional processing if needed
                
            elif menu_type == 'DINNER':
                dinner = Dinner.objects.create(
                    name=menu_details['name'],
                    priceM=menu_details['priceM'],
                    priceL=menu_details['priceL'],
                    fimage=menu_details['image'],
                )
                # Additional processing if needed
                
            elif menu_type == 'SIDE':
                sides = Sides.objects.create(
                    name=menu_details['name'],
                    priceM=menu_details['priceM'],
                    priceL=menu_details['priceL'],
                    fimage=menu_details['image'],
                )
                # Additional processing if needed
            
            # Redirect or show success message
            return redirect('success')  # Redirect to a success URL
            
    else:
        form = MenuCreateForm()

    context = {'form': form}
    return render(request, 'menu/create_menu.html', context)
