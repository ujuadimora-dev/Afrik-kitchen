from django.urls import path
from .views import create_booking, edit_booking, cancel_booking, rebook_booking, booking_list, booking_manager


app_name = 'booking'

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('edit/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('rebook/<int:booking_id>/', rebook_booking, name='rebook_booking'),
    path('list/', booking_list, name='booking_list'),
    path('booking_manager/', booking_manager, name='booking_manager'),
]


