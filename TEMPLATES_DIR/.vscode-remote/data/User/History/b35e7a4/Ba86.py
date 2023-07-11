from django import forms
from .models import Table


class TableAvaliableForm(forms.Form):

     CAPACITY_CHOICES = (
        ("2_person", "2_persons"),
        ("2_person", "3_persons"),
        ( "4_person", "4_persons"),
        ("8_person", "8_persons"),
        ("14_person", "14_persons"),
        ("16_person", "16_persons"),
        ("20_person", "20_persons"),
        ("24_person", "24_persons"),
        ("30_person", "30_persons"),
        ("35_person", "35_persons"),
    )    


    BOOKING_TIME = (
        
        ("8:00am - 9:45am",     "8:00am - 9:45am"),
        ("10:00am - 12:45pm", "10:00am - 12:45pm"),
        ("1:00pm - 2:45pm",     "1:00pm - 2:45pm"),
        ("3:00pm - 5:45pm",     "3:00pm - 5:45pm"),
        ( "7:00pm - 8:45pm",       "7:00pm - 8:45pm"),
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
    

    
