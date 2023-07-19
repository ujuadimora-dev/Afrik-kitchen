from django.contrib import admin
from .models import CreateTable, Booking


# Register your models here.
@admin.register(CreateTable)
class CreateTableAdmin(admin.ModelAdmin):
    list_display = ('table_num', 'capacity', 'table_position', 'wheelchair_accessible')
    # Add other customizations as desired


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'reservation_date', 'reservation_time', 'booked_table', 'number_of_guests')
    # Add other customizations as desired
