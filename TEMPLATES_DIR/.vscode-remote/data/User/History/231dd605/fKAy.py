from django.contrib import admin
from .models import BreakFast, Lunch, Dinner, Sides

# Register your models here.
class BreakFastAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')


admin.site.register(BreakFast, BreakFastAdmin)

admin.site.register(Lunch)

admin.site.register(Dinner)

admin.site.register(Sides)
