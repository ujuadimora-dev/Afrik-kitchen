from django.contrib import admin
from .models import CreateTable, Booking, ManageBooking


# Register your models here.
@admin.register(CreateTable)
class CreateTableAdmin(admin.ModelAdmin):
    list_display = ('table_num', 'capacity', 'table_position', 'wheelchair_accessible')
   


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'reservation_date', 'reservation_time', 'booked_createtable', 'number_of_guests')
    


from django.contrib import admin
from .models import ManageBooking

@admin.register(ManageBooking)
class ManageBookingAdmin(admin.ModelAdmin):
    list_display = ('booked_table', 'number_of_guests')

    def booked_table(self, obj):
        # Replace 'booked_table_field' with the actual field name in the ManageBooking model representing the booked table
        return obj.booked_table_field
    booked_table.short_description = 'Booked Table'

    # Repeat the above process for the 'number_of_guests' field
    def number_of_guests(self, obj):
        # Replace 'number_of_guests_field' with the actual field name in the ManageBooking model representing the number of guests
        return obj.number_of_guests_field
    number_of_guests.short_description = 'Number of Guests'
