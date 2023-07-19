from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Table(models.Model):
    """This is to create the Table for booking"""
    
    CAPACITY_CHOICES = (
        ("2", "2_persons"),
        ("2", "3_persons"),
        ( "4", "4_persons"),
        ("8", "8_persons"),
        ("14", "14_persons"),
        ("20", "20_persons"),
    )

    TABLE_NUMBERS = (
        ("table 2", "2"),
        ("table 3", "3"),
        ("table 4", "4"),
        ("tabele 8", "8"),
        ("table 14", "14"),
        ("table 20", "20"),
    )
    
    TABLE_POSITION = (
        (" is table by window", "Tables by window"),
        (" is in middle", "Tables in middle"),
        (" table in garden", "Tables in the garden"),
        (" table in corridor", "Tables on the corridor"),
    )
    
    BOOKING_TIME = (
        ("8:00am - 9:45am",     "8:00am - 9:45am"),
        ("10:00am - 12:45pm", "10:00am - 12:45pm"),
        ("1:00pm - 2:45pm",     "1:00pm - 2:45pm"),
        ("3:00pm - 5:45pm",     "3:00pm - 5:45pm"),
        ( "7:00pm - 8:45pm",       "7:00pm - 8:45pm"),
    )

    STATUS_CHOICES = (
        ("active", "Active"),
        ("avaliable", "Available"),
        ("not_avaliable", "Not Available"),
    )
   #number = models.IntegerField(default=0)
    table_number = models.CharField(max_length=18, choices=TABLE_NUMBERS, default="2")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="avaliable")
    capacity = models.CharField(max_length=11, choices=CAPACITY_CHOICES, default="2_persons")
    table_position = models.CharField(max_length=25, choices=TABLE_POSITION, default="Tables by window")
    wheelchair_accessible = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.table_number}  ***position** {self.table_position} **for** {self.capacity} number_of_guests'

    


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name


class Booking(models.Model):
    BOOKING_TIME = (
        
        ("8:00am - 9:45am",     "8:00am - 9:45am"),
        ("10:00am - 12:45pm", "10:00am - 12:45pm"),
        ("1:00pm - 2:45pm",     "1:00pm - 2:45pm"),
        ("3:00pm - 5:45pm",     "3:00pm - 5:45pm"),
        ( "7:00pm - 8:45pm",       "7:00pm - 8:45pm"),
    )

    user = models.CharField(max_length=100, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="Customer_name")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default="2")
    reservation_date = models.DateField()
    reservation_time = models.CharField(max_length=20, choices=BOOKING_TIME, default= "8:00am - 9:45am")
    

    def __str__(self):
        return f"{self.customer} **Booking for** {self.table.table_number} on {self.reservation_date} at {self.reservation_time}"
