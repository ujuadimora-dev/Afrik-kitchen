import datetime
from booking.models import Table, Booking


def check_avaliable(table, reservation_date, reservation_time):
    avaliable_list = []  # Fix the variable name here
    booking_list = Booking.objects.filter(table=table)
    for booking in booking_list:
        if booking.reservation_date == reservation_date and booking.reservation_time == reservation_time:
            avaliable_list.append(False)
        else:
            avaliable_list.append(True)  # Update the variable name here
    return all(avaliable_list)


import datetime
from booking.models import Table, Booking

def check_available(table, reservation_date, reservation_time):
    # Convert the reservation date and time into a datetime object
    reservation_datetime = datetime.datetime.combine(reservation_date, reservation_time)

    # Check if there are any bookings for the specified table at the same datetime
    conflicting_bookings = Booking.objects.filter(table=table, datetime=reservation_datetime)

    # If there are no conflicting bookings, the table is available
    if not conflicting_bookings:
        return True
    else:
        return False


import datetime
from booking.models import Table, Booking

def check_available(reservation_date, reservation_time):
    # Convert the reservation date and time into a datetime object
    reservation_datetime = datetime.datetime.combine(reservation_date, reservation_time)

    # Get all the tables
    #all_tables = Table.objects.all()
    booking_list =Table.objects.all()

    # Initialize a list to store the available tables
    available_tables = []

    for booking in booking_list:
        # Check if there are any bookings for the current table at the same datetime
        conflicting_bookings = Booking.objects.filter(table=table, datetime=reservation_datetime)

        # If there are no conflicting bookings, add the table to the list of available tables
        if not conflicting_bookings:
            available_tables.append(table)

    # Return the availability status and the list of available tables
    return len(available_tables) > 0, available_tables
