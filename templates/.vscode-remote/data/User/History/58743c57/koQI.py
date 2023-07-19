from django.urls import path
from .views import BookingList, TableListView, TableDetailView,  create_booking

app_name = 'booking'

urlpatterns = [
    path('table_list/', TableListView, name='TableListView'),
    path('booking_list/', BookingList.as_view(), name='BookingListView'),
    #path('customer_list/', CustomerList.as_view(), name='CustomerList'),
    #path('book/', BookingView.as_view(), name='bookingview'),
    path('table/<capacity>', TableDetailView.as_view(), name='TableDetailView'),
   # path('managebookings/', ManageBooking.as_view(), name='managebookings'),
    path('managebookings/', BookingList.as_view(), name='managebookings'),
    path( 'create_booking/',  create_booking.as_view(), name='create_booking')


]



