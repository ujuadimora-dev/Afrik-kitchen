from django.contrib import admin
from .models import BreakFast, Lunch, Dinner, Sides
#from .forms import BreakFastForm, LunchForm, DinnerForm, SidesForm



# Register your models here.
class BreakFastAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'priceM', 'priceL', 'fimage')


admin.site.register(BreakFast, BreakFastAdmin)


class LunchAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')


admin.site.register(Lunch, LunchAdmin)


class DinnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')


admin.site.register(Dinner, DinnerAdmin)


class SidesAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')


admin.site.register(Sides, SidesAdmin)

""" for creating Menu"""


#admin.site.register(BreakFast, BreakFastAdmin)
#admin.site.register(Lunch, LunchAdmin)
#admin.site.register(Dinner, DinnerAdmin)
#admin.site.register(Sides, SidesAdmin)

