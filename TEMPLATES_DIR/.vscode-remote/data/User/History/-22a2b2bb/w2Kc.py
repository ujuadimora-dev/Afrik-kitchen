from django import forms
from .models import Booking, Table, Customer



""" Avalibiliy form"""
class TableAvailableForm(forms.Form):

    Table_CAPACITY = (

        (2, "2"),
        (3, "3"),
        (4, "4"),
        (14, "14"),
        (20, "20"),
    )
    
    table_num = models.IntegerField(default=0)
    STATUS_CHOICES = (
        ("active", "Active"),
        ("available", "Available"),
        ("not_available", "Not Available"),
    )
    capacity = forms.ChoiceField(choices=capacity, required=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="not_available")
    active_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d %H:%M:%S"])
    ended_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d %H:%M:%S"])



