from django.contrib import admin
from .models import BreakFast, Lunch, Dinner, Sides
from .forms import MenuCreateForm
from .forms import MenuCreateForm, MenuForm

# Register your models here.

class BreakFastAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'description', 
        'priceM', 
        'priceL', 'fimage', 
        'vegetarian', 'calorie_count',
        'created_on', 'created_by_staff')


admin.site.register(BreakFast, BreakFastAdmin)


class LunchAdmin(admin.ModelAdmin):
    list_display =  ('name', 'description', 'priceM', 'priceL', 'fimage', 'vegetarian', 'calorie_count', 'created_on', 'created_by_staff')


admin.site.register(Lunch, LunchAdmin)


class DinnerAdmin(admin.ModelAdmin):
    list_display =  ('name', 'description', 'priceM', 'priceL', 'fimage', 'vegetarian', 'calorie_count', 'created_on', 'created_by_staff')

admin.site.register(Dinner, DinnerAdmin)


class SidesAdmin(admin.ModelAdmin):
    list_display =  ('name', 'description', 'priceM', 'priceL', 'fimage', 'vegetarian', 'calorie_count', 'created_on', 'created_by_staff')


admin.site.register(Sides, SidesAdmin)

""" for creating Menu"""


class MenuAdmin(admin.ModelAdmin):
    form = MenuCreateForm
    list_display = ('breakfast', 'lunch', 'dinnner',('side'))


class MenuAdmin(admin.ModelAdmin):
    form = MenuCreateForm

