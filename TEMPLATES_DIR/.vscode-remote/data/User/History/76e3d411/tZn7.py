from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Table(models.Model):
    """This is to create the Table for booking"""
    
    CAPACITY_CHOICES = (
        ("2_persons", "2_persons"),
        ("3_persons", "3_persons"),
        ( "4_persons", "4_persons"),
        ("8_persons", "8_persons"),
        ("14_persons", "14_persons"),
        ("18_persons", "18_persons"),
        ("20_persons", "20_persons"),
        ("25_persons", "25_persons"),
        ("30_persons", "30_persons"),
    )

    
    
    TABLE_POSITION = (
        (" table by window", "Tables by window"),
        (" table in middle", "Tables in middle"),
        (" table in garden", "Tables in the garden"),
        (" table in corridor", "Tables on the corridor"),
    )
    

    # STATUS_CHOICES = (
    #     ("active", "Active"),
    #     ("avaliable", "Available"),
    #     ("not_avaliable", "Not Available"),
    # )
   #number = models.IntegerField(default=0)
    table_number = models.IntegerField(max_length=18)
    capacity = models.CharField(max_length=11, choices=CAPACITY_CHOICES, default="2_persons")
    table_position = models.CharField(max_length=25, choices=TABLE_POSITION, default="Tables by window")
    wheelchair_accessible = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.table_number}  ***position** {self.table_position} **for** {self.capacity} number_of_guests*** wheelchair_accessible**{self. wheelchair_accessible}** updated_on {self. updated_on}'

    


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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="Customer")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default="2")
    reservation_date = models.DateField()
    reservation_time = models.CharField(max_length=20, choices=BOOKING_TIME, default= "8:00am - 9:45am")
    

    # #def __str__(self):
    #     return f"{self.customer.customer_name} **Booking for** {self.table.table_number} on {self.reservation_date} at {self.reservation_time}"

    def __str__(self):
        return f" **Booking for** {self.table.table_number} on {self.reservation_date} at {self.reservation_time}"


