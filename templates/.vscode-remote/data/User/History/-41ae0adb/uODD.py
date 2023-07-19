from django.shortcuts import render, redirect
from .models import BreakFast, Lunch, Dinner, Sides
from django.conf import settings
from .forms import MenuCreateForm
from django.contrib.auth.decorators import user_passes_test


def index(request):
    """ Renders the index.html template with context variables"""
    ctx = {'name': 'Afrian Kitchen', 'msg': 'This is No 4 projects'}
    return render(request, 'menu/index.html', ctx) 


def menu(request):
    """ Renders the menu.html template"""
    return render(request, 'view_menu/menu.html')


def get_menu_items(model):
    """Retrieves all menu items """
    return model.objects.all()


def render_menu(request, template_name, model):
    """ Renders the menu template """
    menu_items = get_menu_items(model)
    ctx = {model.__name__.lower() + 's': menu_items}
    return render(request, template_name, ctx)


def breakfast(request):
    """ Renders the breakfast.html template with breakfast menu items"""
    return render_menu(request, 'menu/breakfast.html', BreakFast)


def lunch(request):
    """ Renders the lunch.html template with lunch menu items"""
    return render_menu(request, 'menu/lunch.html', Lunch)


def dinner(request):
    """ Renders the dinner.html template with dinner menu items"""
    return render_menu(request, 'menu/dinner.html', Dinner)


def side(request):
    """Renders the side.html template with side menu items"""
    return render_menu(request, 'menu/side.html', Sides)

"""" for the creating the menu"""
@user_passes_test(lambda user: user.is_staff, login_url='includes/403.html') 
def create_menu(request):
    if request.method == 'POST':
        form = MenuCreateForm(request.POST, request.FILES)
        if form.is_valid():
            menu_type = form.cleaned_data['menu_type']
            menu_model = None
            if menu_type == 'BREAKFAST':
                # Save data to the Breakfast model
                menu_model = BreakFast
            elif menu_type == 'LUNCH':
                # Save data to the Lunch model
                menu_model = Lunch
            elif menu_type == 'DINNER':
                # Save data to the Dinner model
                menu_model = Dinner
            elif menu_type == 'SIDE':
                # Save data to the Sides model
                menu_model = Sides

            if menu_model:
                menu = menu_model.objects.create(
                description=form.cleaned_data['description'],
                fimage=form.cleaned_data['fimage'],
                name=form.cleaned_data['name'],
                priceM=form.cleaned_data['priceM'],
                priceL=form.cleaned_data['priceL'],
                vegetarian=form.cleaned_data['vegetarian'],
                calorie_count=form.cleaned_data['calorie_count']
                   
                )
                return render(request, 'menu/success.html', {'menu_type': menu_type.lower()})
    else:
        form = MenuCreateForm()
    
    context = {'form': form}
    return render(request, 'menu/create_menu.html', context)


def menu_success(request):
    """ Renders the menu_success.html template"""
    return render(request, 'menu_success.html')


def permission_denied(request):
    """Renders the permission_denied.html template"""
    return render(request, 'permission_denied.html')









"""" for the creating the menu"""
def staff_check(user):
    return user.is_staff

@user_passes_test(staff_check, login_url='inludes/403.html') 
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
                    fimage=form.cleaned_data['fimage'],
                    name=form.cleaned_data['name'],
                    priceM=form.cleaned_data['priceM'],
                    priceL=form.cleaned_data['priceL'],
                    vegetarian=form.cleaned_data['vegetarian'],
                    calorie_count=form.cleaned_data['calorie_count']
                )
                
                return render(request, 'menu/success.html', {'menu_type': 'breakfast'})
                
            elif menu_type == 'LUNCH':
                # Save data to Lunch model
                lunch = Lunch.objects.create(
                    description=form.cleaned_data['description'],
                    fimage=form.cleaned_data['fimage'],
                    name=form.cleaned_data['name'],
                    priceM=form.cleaned_data['priceM'],
                    priceL=form.cleaned_data['priceL'],
                    vegetarian=form.cleaned_data['vegetarian'],
                    calorie_count=form.cleaned_data['calorie_count']
                )
                
                return render(request, 'menu/success.html', {'menu_type': 'lunch'})
                
            elif menu_type == 'DINNER':
                # Save data to Dinner model
                dinner = Dinner.objects.create(
                    description=form.cleaned_data['description'],
                    fimage=form.cleaned_data['fimage'],
                    name=form.cleaned_data['name'],
                    priceM=form.cleaned_data['priceM'],
                    priceL=form.cleaned_data['priceL'],
                    vegetarian=form.cleaned_data['vegetarian'],
                    calorie_count=form.cleaned_data['calorie_count']
                )
               
                return render(request, 'menu/success.html', {'menu_type': 'dinner'})
                
            elif menu_type == 'SIDE':
                # Save data to Sides model
                sides = Sides.objects.create(
                    description=form.cleaned_data['description'],
                    fimage=form.cleaned_data['fimage'],
                    name=form.cleaned_data['name'],
                    priceM=form.cleaned_data['priceM'],
                    priceL=form.cleaned_data['priceL'],
                    vegetarian=form.cleaned_data['vegetarian'],
                    calorie_count=form.cleaned_data['calorie_count']
                )
             
                return render(request, 'menu/success.html', {'menu_type': 'side'})
    else:
        form = MenuCreateForm()

    

    context = {'form': form}
    return render(request, 'menu/create_menu.html', context)


def menu_success(request):
    return render(request, 'menu_success.html')

def permission_denied(request):
    return render(request, 'permission_denied.html')


#############################

from django.shortcuts import render, redirect
from .models import BreakFast, Lunch, Dinner, Sides
from django.conf import settings
from .forms import MenuCreateForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def index(request):
    # Renders the index.html template with context variables
    ctx = {'name': 'African Kitchen', 'msg': 'This is No 4 projects'}
    return render(request, 'menu/index.html', ctx)

def menu(request):
    # Renders the menu.html template
    return render(request, 'view_menu/menu.html')

def get_menu_items(model):
    # Retrieves all menu items for the given model
    return model.objects.all()

def render_menu(request, template_name, model):
    # Renders the menu template with the appropriate model and context
    menu_items = get_menu_items(model)
    ctx = {model.__name__.lower() + 's': menu_items}
    return render(request, template_name, ctx)

def breakfast(request):
    # Renders the breakfast.html template with breakfast menu items
    return render_menu(request, 'menu/breakfast.html', BreakFast)

def lunch(request):
    # Renders the lunch.html template with lunch menu items
    return render_menu(request, 'menu/lunch.html', Lunch)

def dinner(request):
    # Renders the dinner.html template with dinner menu items
    return render_menu(request, 'menu/dinner.html', Dinner)

def side(request):
    # Renders the side.html template with side menu items
    return render_menu(request, 'menu/side.html', Sides)

@user_passes_test(lambda user: user.is_staff, login_url='includes/403.html') 
def create_menu(request):
    if request.method == 'POST':
        form = MenuCreateForm(request.POST, request.FILES)
        if form.is_valid():
            menu_type = form.cleaned_data['menu_type']
            menu_model = None
            if menu_type == 'BREAKFAST':
                # Save data to the Breakfast model
                menu_model = BreakFast
            elif menu_type == 'LUNCH':
                # Save data to the Lunch model
                menu_model = Lunch
            elif menu_type == 'DINNER':
                # Save data to the Dinner model
                menu_model = Dinner
            elif menu_type == 'SIDE':
                # Save data to the Sides model
                menu_model = Sides
            
            if menu_model:
                menu = menu_model.objects.create(
                    description=form.cleaned_data['description'],
                    fimage=form.cleaned_data['fimage'],
                    name=form.cleaned_data['name'],
                    priceM=form.cleaned_data['priceM'],
                    priceL=form.cleaned_data['priceL'],
                    vegetarian=form.cleaned_data['vegetarian'],
                    calorie_count=form.cleaned_data['calorie_count']
                )
                return render(request, 'menu/success.html', {'menu_type': menu_type.lower()})
    else:
        form = MenuCreateForm()
    
    context = {'form': form}
    return render(request, 'menu/create_menu.html', context)

def menu_success(request):
    # Renders the menu_success.html template
    return render(request, 'menu_success.html')

def permission_denied(request):
    # Renders the permission_denied.html template
    return render(request, 'permission_denied.html')
