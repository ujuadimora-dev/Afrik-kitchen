from django.urls import path
from .views import create_booking, edit_booking, cancel_booking, rebook_booking, booking_list, booking_manager
from .import views

app_name = 'booking'

urlpatterns = [
    path('create/', views.create_booking.as views(), name='create_booking'),
    path('edit/<int:booking_id>/', edit_booking.as views(), name='edit_booking'),
    path('cancel/<int:booking_id>/', cancel_booking.as views(), name='cancel_booking'),
    path('rebook/<int:booking_id>/', rebook_booking.as views(), name='rebook_booking'),
    path('list/', views.booking_list.as views(), name='booking_list'),
    path('booking_manager/', views.booking_manager.as views(), name='booking_manager'),
]


