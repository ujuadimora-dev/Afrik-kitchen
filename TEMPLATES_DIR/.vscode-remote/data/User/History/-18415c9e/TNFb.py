import datetime
from booking.models import Table, Booking


def check_available(table, reservation_date, reservation_time):
    available_list = []
    booking_list = Booking.objects.filter(table=table)
    for booking in booking_list:
        if booking.reservation_date == reservation_date and booking.reservation_time == reservation_time:
            available_list.append(False)
        else:
            available_list.append(True)
    return all(available_list)
