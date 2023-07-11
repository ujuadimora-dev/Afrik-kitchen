from django.contrib import admin
from .models import CreateTable, Booking, ManageBooking


# Register your models here.
@admin.register(CreateTable)
class CreateTableAdmin(admin.ModelAdmin):
    list_display = ('table_num', 'capacity', 'table_position', 'wheelchair_accessible')
   


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'reservation_date', 'reservation_time', 'booked_table', 'number_of_guests')
    

@admin.register(ManageBooking)
class ManageBookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'reservation_date', 'reservation_time', 'booked_table', 'number_of_guests')
    
