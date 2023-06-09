from django.contrib import admin
from .models import FoodMenu, Menu



#admin.site.register(FoodMenu)

# Register your models here.

@admin.register(FoodMenu)
class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image')
    list_filter = ('name',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_by', 'created_on', 'updated_on')
    list_filter = ('name',)


    def get_items(self, obj):
        """ Function to return all menu items in many to many """
        return "\n, ".join([m._food_name for m in obj.food_menu.all()])

        #return "\n, ".join([m._item_name for m in obj.menu_items.all()])


