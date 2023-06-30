from django.contrib import admin

# Register your models h


from django.contrib import admin
from .models import Table, Booking 

admin.site.register(Booking)
admin.site.register(Table)
#admin.site.register(Customer)
