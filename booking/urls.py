from django.urls import path
from .views import Booking
from booking.views import BookingList, CreateTableList, ManageBookingList

app_name = 'booking'

urlpatterns = [
    path('booking/booking_list/', BookingList.as_view(), name='BookingList'),
    path('booking/createtable_list/', CreateTableList.as_view(), name='CreateTableList'),
    path('booking/managebooking_list/', ManageBookingList.as_view(), name='ManageBookingList')
]



