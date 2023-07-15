# from django.shortcuts import render, redirect
# from .models import BreakFast, Lunch, Dinner, Sides
# from django.conf import settings
# from .forms import MenuCreateForm, MenuDeleteForm
# from django.contrib.auth.decorators import user_passes_test
# from django.http import Http404
# from django.urls import reverse, reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.views.generic import UpdateView, DeleteView
# from django.shortcuts import get_object_or_404
# from view_menu.models import MenuItem



# # def index(request):
# #     """ Renders the index.html template with context variables"""
# #     ctx = {'name': 'Afrian Kitchen', 'msg': 'This is No 4 projects'}
# #     return render(request, 'menu/index.html', ctx) 


# # def menu(request):
# #     """ Renders the menu.html template"""
# #     return render(request, 'view_menu/menu.html')


# # def get_menu_items(model):
# #     """Retrieves all menu items """
# #     return model.objects.all()


# # def render_menu(request, template_name, model):
# #     menu_items = get_menu_items(model)
# #     ctx = {model.__name__.lower() + 's': menu_items, 'sides': menu_items}  # Add 'sides' in the context
# #     return render(request, template_name, ctx)



# # def breakfast(request):
# #     """ Renders the breakfast.html template with breakfast menu items"""
# #     return render_menu(request, 'menu/breakfast.html', BreakFast)


# # def lunch(request):
# #     """ Renders the lunch.html template with lunch menu items"""
# #     return render_menu(request, 'menu/lunch.html', Lunch)


# # def dinner(request):
# #     """ Renders the dinner.html template with dinner menu items"""
# #     return render_menu(request, 'menu/dinner.html', Dinner)


# # def side(request):
# #     """Renders the side.html template with side menu items"""
# #     return render_menu(request, 'menu/side.html', Sides)

# # """" for the creating the menu"""
# # @user_passes_test(lambda user: user.is_staff, login_url='includes/403.html') 
# # def create_menu(request):
# #     if request.method == 'POST':
# #         form = MenuCreateForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             menu_type = form.cleaned_data['menu_type']
# #             menu_model = None
# #             if menu_type == 'BREAKFAST':
# #                 # Save data to the Breakfast model
# #                 menu_model = BreakFast
# #             elif menu_type == 'LUNCH':
# #                 # Save data to the Lunch model
# #                 menu_model = Lunch
# #             elif menu_type == 'DINNER':
# #                 # Save data to the Dinner model
# #                 menu_model = Dinner
# #             elif menu_type == 'SIDE':
# #                 # Save data to the Sides model
# #                 menu_model = Sides

# #             if menu_model:
# #                 menu = menu_model.objects.create(
# #                     description=form.cleaned_data['description'],
# #                     fimage=form.cleaned_data['fimage'],
# #                     name=form.cleaned_data['name'],
# #                     priceM=form.cleaned_data['priceM'],
# #                     priceL=form.cleaned_data['priceL'],
# #                     vegetarian=form.cleaned_data['vegetarian'],
# #                     calorie_count=form.cleaned_data['calorie_count']
                   
# #                 )
# #                 return render(request, 'menu/success.html',
# #                 {'menu_type':menu_type.lower()})
# #     else:
# #         form = MenuCreateForm()
    
# #     context = {'form': form}
# #     return render(request, 'menu/create_menu.html', context)


# # def menu_success(request):
# #     """ Renders the menu_success.html template"""
# #     return render(request, 'menu_success.html')


# # def permission_denied(request):
# #     """Renders the permission_denied.html templae"""
# #     return render(request, 'permission_denied.html')


# # def page_not_found(request):
# #     return render(request, 'menu/page_not_found.html')


# # def manage_menu(request):
# #     view_menu = view_Menu.objects.all()
# #     return render(request, 'manage_menu.html', {'view_menus': view_menus})


# # class EditMenuView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
# #     """
# #     A view to provide a Form to the user
# #     to edit a menu
# #     """
# #     form_class = MenuCreateForm
# #     template_name = 'menu/edit_menu.html'
# #     #success_url = "/view_menu/manage_menu"
# #     success_url = reverse_lazy('view_menu:manage_menus')
# #     model = 'view_menu'


# #     def form_valid(self, form):
      
# #         messages(
# #             self.request,
# #             'Successfully updated menu'
# #         )
# #         return super(EditMenuView, self).form_valid(form)

# #     def test_func(self):
# #         """ Check user is staff else throw 403 """
# #         return self.request.user.is_staff


# # class DeleteMenuView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
# #     """ A view to delete a menu """
# #     model = 'view_menu'
# #     template_name = 'menu/delete_menu.html'
# #     success_url = "/menu/manage_menu"

# #     def form_valid(self, form):
# #         """ Display toast message on form success """
# #         messages(
# #             self.request,
# #             'Successfully deleted menu'
# #         )
# #         return super(DeleteMenuView, self).form_valid(form)

# #     def test_func(self):
# #         """ Test user is staff else throw 403 """
# #         return self.request.user.is_staff


# from django.shortcuts import render, redirect
# from django.contrib import messages
# #rom .models import BreakFast, Lunch, Dinner, Sides, view_Menu
# from .forms import MenuCreateForm
# from django.contrib.auth.decorators import user_passes_test
# from django.urls import reverse_lazy
# from .models import MenuItem
# # from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# # from django.views.generic import UpdateView, DeleteView
# # from django.shortcuts import render
# # from .models import MenuItem
# # from .models import BreakFast, Lunch, Dinner, Sides
# # from django.views.generic.detail import DetailView
# # from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# # from django.views.generic.edit import UpdateView
# # from .forms import MenuCreateForm, MenuEditForm
#   #from .models import MenuItem
# # #from view_menu.models import MenuItem
# # #from django.shortcuts import get_object_or_404




# def index(request):
#     """ Renders the index.html template with context variables"""
#     ctx = {'name': 'Afrian Kitchen', 'msg': 'This is No 4 projects'}
#     return render(request, 'menu/index.html', ctx) 


# def menu(request):
#     """ Renders the menu.html template"""
#     return render(request, 'view_menu/menu.html')


# def get_menu_items(model):
#     """Retrieves all menu items """
#     return model.objects.all()


# def render_menu(request, template_name, model):
#     menu_items = get_menu_items(model)
#     ctx = {model.__name__.lower() + 's': menu_items, 'sides': menu_items}
#     return render(request, template_name, ctx)


# def breakfast(request):
#     """ Renders the breakfast.html template with breakfast menu items"""
#     return render_menu(request, 'menu/breakfast.html', BreakFast)


# def lunch(request):
#     """ Renders the lunch.html template with lunch menu items"""
#     return render_menu(request, 'menu/lunch.html', Lunch)


# def dinner(request):
#     """ Renders the dinner.html template with dinner menu items"""
#     return render_menu(request, 'menu/dinner.html', Dinner)


# def side(request):
#     """ Renders the side.html template with side menu items"""
#     return render_menu(request, 'menu/side.html', Sides)


# @user_passes_test(lambda user: user.is_staff, login_url='includes/403.html') 
# def create_menu(request):
#     if request.method == 'POST':
#         form = MenuCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             menu_type = form.cleaned_data['menu_type']
#             menu_model = None
#             if menu_type == 'BREAKFAST':
#                 menu_model = BreakFast
#             elif menu_type == 'LUNCH':
#                 menu_model = Lunch
#             elif menu_type == 'DINNER':
#                 menu_model = Dinner
#             elif menu_type == 'SIDE':
#                 menu_model = Sides

#             if menu_model:
#                 menu = menu_model.objects.create(
#                     description=form.cleaned_data['description'],
#                     fimage=form.cleaned_data['fimage'],
#                     name=form.cleaned_data['name'],
#                     priceM=form.cleaned_data['priceM'],
#                     priceL=form.cleaned_data['priceL'],
#                     vegetarian=form.cleaned_data['vegetarian'],
#                     calorie_count=form.cleaned_data['calorie_count']
#                 )
#                 return render(request, 'menu/success.html', {'menu_type': menu_type.lower()})
#     else:
#         form = MenuCreateForm()
    
#     context = {'form': form}
#     return render(request, 'menu/create_menu.html', context)


# def menu_success(request):
#     """ Renders the menu_success.html template"""
#     return render(request, 'menu_success.html')


# def permission_denied(request):
#     """ Renders the permission_denied.html template"""
#     return render(request, 'permission_denied.html')


# def page_not_found(request):
#     return render(request, 'menu/page_not_found.html')

 
# from .models import MenuItem, BreakFast, Lunch, Dinner, Sides

# from .models import BreakFast, Lunch, Dinner, Sides

# def manage_menu(request):
#     menu_data = {}

#     # Retrieve all menu items
#     breakfast_items = BreakFast.objects.all()
#     lunch_items = Lunch.objects.all()
#     dinner_items = Dinner.objects.all()
#     sides_items = Sides.objects.all()

#     menu_data['Breakfast'] = breakfast_items
#     menu_data['Lunch'] = lunch_items
#     menu_data['Dinner'] = dinner_items
#     menu_data['Sides'] = sides_items

#     context = {
#         'menu_data': menu_data
#     }
#     return render(request, 'manage_menu.html', context)


# from django.shortcuts import render, get_object_or_404, redirect
# from .models import MenuItem
# from .forms import MenuItemForm

# from django.shortcuts import render, get_object_or_404, redirect
# from .models import MenuItem
# from .forms import MenuItemForm

# def delete_menu_item(request, menuitem_id):
#     menu_item = get_object_or_404(MenuItem, pk=menuitem_id)

#     if request.method == 'POST':
#         menu_item.delete()
#         # Redirect to success page or render a success message

#     context = {'menu_item': menu_item}
#     return render(request, 'menu/delete_menu_item.html', context)

# def edit_menu_item(request, menuitem_id):
#     menu_item = get_object_or_404(MenuItem, pk=menuitem_id)
#     if request.method == 'POST':
#         form = MenuItemForm(request.POST, instance=menu_item)
#         if form.is_valid():
#             form.save()
#             # Redirect to success page or render a success message
#     else:
#         form = MenuItemForm(instance=menu_item)
#     context = {'form': form, 'menu_item': menu_item}
#     return render(request, 'menu/edit_menu_item.html', context)











     
# # def edit_menu(request, menuitem_id):
# #     try:
# #         menu_item = get_object_or_404(MenuItem, pk=menuitem_id)
# #         return render(request, 'menu/edit_menu.html', {'menu_item': menu_item})
# #     except MenuItem.DoesNotExist:
# #         # Handle the case when the MenuItem object does not exist
# #         return HttpResponse("Menu item does not exist.")
# #     except Exception as e:
# #         # Handle other exceptions
# #         return HttpResponse(f"An error occurred: {str(e)}")

# # class EditMenuView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
# #     """
# #     A view to provide a form to the user to edit a menu
# #     """
# #     model = MenuItem
# #     form_class = MenuEditForm
# #     template_name = 'menu/edit_menu.html'
# #     success_url = reverse_lazy('view_menu:manage_menus')

# #     def get_queryset(self):
# #         queryset = super().get_queryset()
# #         # Add any additional filters or annotations to the queryset if needed
# #         return queryset

# #     def test_func(self):
# #         menu_item = self.get_object()
# #         return menu_item.created_by_staff == self.request.user.username

# #     def form_valid(self, form):
# #         messages.success(self.request, 'Successfully updated menu')
# #         return super().form_valid(form)


# # class DeleteMenuView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
# #     """ A view to delete a menu """
# #     model = 'view_menu'
# #     template_name = 'menu/delete_menu.html'
# #     success_url = reverse_lazy('view_menu:manage_menus')

# #     def form_valid(self, form):
# #         messages.success(self.request, 'Successfully deleted menu')
# #         return super().form_valid(form)

# #     def test_func(self):
# #         """ Check if the user is staff else throw 403 """
# #         return self.request.user.is_staff
