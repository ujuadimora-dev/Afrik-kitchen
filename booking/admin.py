from django.contrib import admin


from django.contrib import admin
from .models import Table, Booking 

admin.site.register(Booking)
admin.site.register(Table)

