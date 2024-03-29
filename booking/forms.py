from django import forms
from .models import Table


class TableAvaliableForm(forms.Form):
    """ for form Avalaiblity for table booking"""
    
    BOOKING_TIME = (
        ("8:00am - 9:45am", "8:00am - 9:45am"),
        ("10:00am - 12:45pm", "10:00am - 12:45pm"),
        ("1:00pm - 2:45pm", "1:00pm - 2:45pm"),
        ("3:00pm - 5:45pm", "3:00pm - 5:45pm"),
        ("7:00pm - 8:45pm", "7:00pm - 8:45pm"),
    )

    reservation_date = forms.DateField(
        label='Reservation Date',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=["%Y-%m-%d"],
        required=True
    )
    reservation_time = forms.ChoiceField(
        choices=BOOKING_TIME,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
