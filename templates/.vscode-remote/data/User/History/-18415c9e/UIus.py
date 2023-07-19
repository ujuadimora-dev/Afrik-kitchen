import datetime
from booking.models import Table, Booking


import datetime
from booking.models import Table, Booking


def check_available(table, reservation_date, reservation_time):
    booking_list = Booking.objects.filter(table=table)
    for booking in booking_list:
        if booking.reservation_date == reservation_date and booking.reservation_time == reservation_time:
            return False, "This table is already booked. Please select another one."
    return True, "This table is available for booking."



