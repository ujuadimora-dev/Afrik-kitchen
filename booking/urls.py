from django.urls import path
from .views import BookingList, TableListView, TableDetailView
from .views import BookingCreateView, BookingSuccessView, CancelBookingView
from .views import DeleteBookingView, EditBookingView
from .views import CancelBookingView,  DeleteBookingView, BookedAlredyView, managebooking
from . import views


app_name = 'booking'

urlpatterns = [
    path('table_list/', TableListView, name='TableListView'),
    path('booking_list/', BookingList.as_view(), name='BookingListView'),
    path('table/<capacity>', TableDetailView.as_view(), name='TableDetailView'),
    path('managebookings/', managebooking, name='managebookings'),
    path('create/', BookingCreateView.as_view(), name='create_booking'),
    path('success/', BookingSuccessView.as_view(), name='booking_success'),
    path('booked/', BookedAlredyView.as_view(), name='already_booked'),
    path('cancel/<int:pk>/', CancelBookingView.as_view(), name='cancel_booking'),
    path('delete/<int:pk>/', DeleteBookingView.as_view(), name='delete_booking'),
    path('edit/<int:pk>/', EditBookingView.as_view(), name='booking_edit'),   



    

]

