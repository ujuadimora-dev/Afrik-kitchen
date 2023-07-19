from django import forms
from .models import Booking, Table, Customer

""" Avalibiliy form"""
class TableAvailableForm(forms.Form):

    CAPACITY_CHOICES = (

        (2, "2"),
        (3, "3"),
        (4, "4"),
        (14, "14"),
        (20, "20"),
    )
    
    capacity = forms.ChoiceField(choices=CAPACITY_CHOICES, required=True)
    reservation_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d %H:%M:%S"])
    reservation_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d %H:%M:%S"])



