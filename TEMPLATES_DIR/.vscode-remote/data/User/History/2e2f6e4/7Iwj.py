from django.contrib import admin
from .models import BreakFast, Lunch, Dinner, Sides

# Register your models here.
admin.site.register(BreakFast)

admin.site.register(Lunch)

admin.site.register(Dinner)

admin.site.register(Sides)
