from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'reservation_date', 'reservation_time', 'booked_table', 'number_of_guests']
