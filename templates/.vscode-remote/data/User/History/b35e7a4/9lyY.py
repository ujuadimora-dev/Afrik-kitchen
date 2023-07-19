from django import forms
from .models import Table


class TableAvaliableForm(forms.Form):

    CAPACITY_CHOICES = (
        ("2", "2_persons"),
        ("2", "3_persons"),
        ( "4", "4_persons"),
        ("8", "8_persons"),
        ("14", "14_persons"),
        ("20", "20_persons"),
    )


    capacity_choices = forms.ChoiceField(choices=CAPACITY_CHOICES, required=True)
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
    

    
