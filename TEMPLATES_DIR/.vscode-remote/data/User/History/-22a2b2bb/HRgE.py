from django import forms
from .models import Booking, Table, Customer

""" Avalibiliy form"""
class TableAvaliableForm(forms.Form):

    CAPACITY_CHOICES = (

        (2, "2"),
        (3, "3"),
        (4, "4"),
        (14, "14"),
        (20, "20"),
    )

    TABLE_POSITION = (
        ("window", "Tables near the window"),
        ("middle", "Tables in the middle"),
        ("outside", "Tables outside in the garden"),
        ("corridor", "Tables on the corridor"),
    )

    BOOKING_TIME = (
        (1, "8:00am - 9:45am"),
        (2, "10:00am - 12:45pm"),
        (3, "1:00pm - 2:45pm"),
        (4, "3:00pm - 5:45pm"),
        (5, "7:00pm - 8:45pm"),
    )

    
        model = Table
        fields = ['reservation_date']
        widgets = {
            'reservation_date': forms.DateInput(format='%Y-%m-%d'),
        }
    


    capacity = forms.ChoiceField(choices=CAPACITY_CHOICES, required=True)
    reservation_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d %H:%M:%S"])
    reservation_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d %H:%M:%S"])



