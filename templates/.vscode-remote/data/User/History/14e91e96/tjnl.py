from django.urls import path
from .views import create_booking, edit_booking, cancel_booking, rebook_booking, booking_list

urlpatterns = [
    path('booking/create/', create_booking, name='create_booking'),
    path('booking/edit/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('booking/cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('booking/rebook/<int:booking_id>/', rebook_booking, name='rebook_booking'),
    path('booking/list/', booking_list, name='booking_list'),
    path('booking_manager/', booking_manager, name='booking_manager'),
]


from django.urls import path
from .views import booking_manager

urlpatterns = [
    path('booking_manager/', booking_manager, name='booking_manager'),
    # Other URL patterns...
]
