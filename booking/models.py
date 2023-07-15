from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import redirect


class Table(models.Model):
    """This is to create the Table for booking"""
    
    CAPACITY_CHOICES = (
        ("2_person", "2_persons"),
       # ("3_person", "3_persons"),
        ( "4_person", "4_persons"),
       ("8_person", "8_persons"),
        #("14_person", "14_persons"),
       ("16_person", "16_persons"),
       # ("20_person", "20_persons"),
        ("24_person", "24_persons"),
        #("30_person", "30_persons"),
        ("35_person", "35_persons"),
        

    )

    # 'TABLE_NUMBERS = (
    #     ("table 2", "2"),
    #     ("table 3", "3"),
    #     ("table 4", "4"),
    #     ("tabele 8", "8"),
    #     ("table 14", "14"),
    #     ("table 20", "20"),
    # )'
    
    TABLE_POSITION = (
        ("  by side of the window", "by side of the  window"),
        ("  in middle of the room", " in middle"),
        ("  in Resturant garden", "in Resturant garden"),
        ("  on the corridor", " on the corridor"),
    )
    
    # BOOKING_TIME = (
    #     ("8:00am - 9:45am",     "8:00am - 9:45am"),
    #     ("10:00am - 12:45pm", "10:00am - 12:45pm"),
    #     ("1:00pm - 2:45pm",     "1:00pm - 2:45pm"),
    #     ("3:00pm - 5:45pm",     "3:00pm - 5:45pm"),
    #     ( "7:00pm - 8:45pm",       "7:00pm - 8:45pm"),
    # )

    
    table_number = models.IntegerField()
   
    capacity = models.CharField(max_length=11, choices=CAPACITY_CHOICES, default="2_persons")
    table_position = models.CharField(max_length=25, choices=TABLE_POSITION, default="Tables by window")
    wheelchair_accessible = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' Table {self.table_number}  *** with position** {self.table_position} **wheelchair_accessiblity**{self.wheelchair_accessible} **for** {self.capacity} number_of_guests'

    

class Booking(models.Model):
    BOOKING_TIME = (
        
        ("8:00am - 9:45am",     "8:00am - 9:45am"),
        ("10:00am - 12:45pm", "10:00am - 12:45pm"),
        ("1:00pm - 2:45pm",     "1:00pm - 2:45pm"),
        ("3:00pm - 5:45pm",     "3:00pm - 5:45pm"),
        ( "7:00pm - 8:45pm",       "7:00pm - 8:45pm"),
  )  

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)        
   
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.CharField(max_length=20, choices=BOOKING_TIME, default= "8:00am - 9:45am")
    

    
    def __str__(self):
       return f"{self.user} Sucessfully **has Booked for** {self.table.table_number} Table  on {self.reservation_date} at {self.reservation_time}"
    


    def get_table_capacity(self):
        """ to get the value to display"""
        table_capacities = dict(self.table.CAPACITY_CHOICES)
        table_capacity = table_capacities.get(self.table.capacity)
        return table_capacity


