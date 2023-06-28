from django.db import models
from django.db import models
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
        ("mon", "8:00am - 9:45am"),
        ("mid_mon", "10:00am - 12:45pm"),
        ("noon", "1:00pm - 2:45pm"),
        ("late_noon", "3:00pm - 5:45pm"),
        ("eve", "7:00pm - 8:45pm"),
    )

    STATUS_CHOICES = (
        ("active", "Active"),
        ("available", "Available"),
        ("not_available", "Not Available"),
    )
   #number = models.IntegerField(default=0)
    table_number = models.CharField(max_length=18, choices=TABLE_NUMBERS, default="2")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    capacity = models.CharField(max_length=11, choices=CAPACITY_CHOICES, default="2_persons")
    table_position = models.CharField(max_length=25, choices=TABLE_POSITION, default="Tables by window")
    wheelchair_accessible = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.table_number}.{self.status} on {self.table_position} for {self.capacity} number_of_guests'

    


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name


class Booking(models.Model):
    BOOKING_TIME = (
        (1, "8:00am - 9:45am"),
        (2, "10:00am - 12:45pm"),
        (3, "1:00pm - 2:45pm"),
        (4, "3:00pm - 5:45pm"),
        (5, "7:00pm - 8:45pm"),
    )

    customer_name = models.CharField(max_length=100, default="Dan Obi")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings_as_customer', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings_as_user', default=1)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=2)
    number_of_guests = models.IntegerField(default=1)
    reservation_date = models.DateField(auto_now_add=True) 
    reservation_time = models.IntegerField(choices=BOOKING_TIME, default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for Table {self.table.table_num} on {self.reservation_date}"
