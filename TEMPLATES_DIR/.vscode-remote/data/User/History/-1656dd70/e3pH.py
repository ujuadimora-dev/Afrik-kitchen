from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Table(models.Model):
    """This is to create the Table for booking"""
    
    CAPACITY_CHOICES = (
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (8, "8"),
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

    table_num = models.IntegerField(default=0)
    STATUS_CHOICES = (
        ("active", "Active"),
        ("available", "Available"),
        ("not_available", "Not Available"),
    )
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="not_available")
    capacity = models.IntegerField(choices=CAPACITY_CHOICES, default=2)
    table_position = models.CharField(max_length=10, choices=TABLE_POSITION, default="window")
    wheelchair_accessible = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.table_num)

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name


class Booking(models.Model):
    """This is to create the Booking model"""

    BOOKING_TIME = (
        (1, "8:00am - 9:45am"),
        (2, "10:00am - 12:45pm"),
        (3, "1:00pm - 2:45pm"),
        (4, "3:00pm - 5:45pm"),
        (5, "7:00pm - 8:45pm"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=2)
    number_of_guests = models.IntegerField(default=1)
    reservation_date = models.DateField(auto_now_add=True) 
    reservation_time = models.IntegerField(choices=BOOKING_TIME, default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for Table {self.table.table_num} on {self.reservation_date}"



    





