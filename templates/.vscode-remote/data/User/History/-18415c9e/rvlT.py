import datetime
from booking.models import Table, Booking


def check_avaliable(table, active_time, ended_time):
    available_list = []
    Booking_list = Booking.objects.filter(table=table)
    for booking in booking_list:
        if booking.active_time > ended_time or booking. ended_time < active_time:
            available_list.append(True)
        else:
            available_list.append(False)
    return all(available_list)