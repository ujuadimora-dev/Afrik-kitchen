from django.urls import path
from .views import BookingList, TableListView, TableDetailView, BookingCreateView, BookingSuccessView, CancelBookingView,  DeleteBookingView
from . import views


app_name = 'booking'

urlpatterns = [
    path('table_list/', TableListView, name='TableListView'),
    path('booking_list/', BookingList.as_view(), name='BookingListView'),
    #path('customer_list/', CustomerList.as_view(), name='CustomerList'),
    #path('book/', BookingView.as_view(), name='bookingview'),
    path('table/<capacity>', TableDetailView.as_view(), name='TableDetailView'),
   # path('managebookings/', ManageBooking.as_view(), name='managebookings'),
    path('managebookings/', BookingList.as_view(), name='managebookings'),
    path('create/', BookingCreateView.as_view(), name='create_booking'),
    path('success/', BookingSuccessView.as_view(), name='booking_success'),

    path('cancel/<int:pk>/', CancelBookingView.as_view(), name='cancel_booking'),
    path('delete/<int:pk>/', DeleteBookingView.as_view(), name='delete_booking'),


]

