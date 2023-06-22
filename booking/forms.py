from django import forms
from booking.models import Booking
#from booking.forms import BookingForm
#from .forms import BookingForm




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'reservation_date', 'reservation_time', 'booked_table', 'number_of_guests']
