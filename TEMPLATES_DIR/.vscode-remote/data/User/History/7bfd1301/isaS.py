# import datetime
# from booking.models import Table, Booking


# def check_avaliable(table, reservation_date, reservation_time):
#     avaliable_list = []  # Fix the variable name here
#     booking_list = Booking.objects.filter(table=table)
#     for booking in booking_list:
#         if booking.reservation_date == reservation_date and booking.reservation_time == reservation_time:
#             avaliable_list.append(False)
#         else:
#             avaliable_list.append(True)  # Update the variable name here
#     return all(avaliable_list)


