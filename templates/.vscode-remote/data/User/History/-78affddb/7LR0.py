from django.contrib import admin
from .models import CreateTable, Booking, ManageBooking, Customer


# Register your models here.
@admin.register(CreateTable)
class CreateTableAdmin(admin.ModelAdmin):
    list_display = ('status', 'table_num', 'capacity', 'table_position', 'wheelchair_accessible',
    'created_on', 'updated_on', 'content')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'phone_number', 'create_table')



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'reservation_date', 'reservation_time', 'booked_createtable', 'number_of_guests')
    
    def save_model(self, request, obj, form, change):
        # Check if the selected table is already booked at the given date and time
        existing_booking = Booking.objects.filter(table=obj.table, date=obj.date, time=obj.time).exists()

        if existing_booking and not change:
            # If a booking already exists for the table at the same date and time, raise a validation error
            raise ValidationError('Table is already booked at the selected date and time.')

        obj.save()
        

@admin.register(ManageBooking)
class ManageBookingAdmin(admin.ModelAdmin):
    list_display = ('booked_createtable', 'number_of_guests')

    def booked_createtable(self, obj):
        # Replace 'booked_table_field' with the actual field name in the ManageBooking model representing the booked table
        return obj.booked_table_field
    booked_createtable.short_description = 'Booked CreateTable'

    # Repeat the above process for the 'number_of_guests' field
    def number_of_guests(self, obj):
        # Replace 'number_of_guests_field' with the actual field name in the ManageBooking model representing the number of guests
        return obj.number_of_guests_field
    number_of_guests.short_description = 'Number of Guests'
