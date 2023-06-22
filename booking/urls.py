from django.urls import path
from .views import CreateBookingView, Booking, SuccessView
from . import views


app_name = 'booking'


urlpatterns = [
    path('create_booking/', CreateBookingView.as_view(), name='create_booking'),
    path('success/', views.SuccessView, name='success'),
    
    #path('booking/', views.booking, name='booking'),
    # Other URL patterns
]


