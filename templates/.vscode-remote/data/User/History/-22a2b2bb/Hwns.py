from django import forms
from .models import Booking, Table, Customer, CAPACITY

""" Avalibiliy form"""
class TableAvailableForm(forms.Form):

    CAPACITY = (

        (2, "2"),
        (3, "3"),
        (4, "4"),
        (14, "14"),
        (20, "20"),
    )
    
    
    capacity = forms.IntegerField(choices=CAPACITY, required=True)
    active_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d %H:%M:%S"])
    ended_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d %H:%M:%S"])



