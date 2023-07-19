from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Table(models.Model):
    """This is to create the Table for booking"""
    
    CAPACITY_CHOICES= (
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
    created_on = models.DateTimeField(auto_now_add=True)
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
    """Model to create a booking"""
    #createtable = models.OneToOneField(CreateTable, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #customer_name = models.CharField(max_length=20, null=True)
    table = models.ForeignKey(Table, related_name='bookings', on_delete=models.CASCADE, default=0)
    table_num = models.ForeignKey(Table, related_name='booking_numbers', on_delete=models.CASCADE, default=0)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True )
    number_of_guests = models.IntegerField(default=2)
    reservation_date = models.DateField()
    reservation_time = models.IntegerField(choices=BOOKING_TIME, default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Order by customer_name and then reservation_time"""
        ordering = ['customer_name', 'reservation_time',  'reservation_date']

    def __str__(self):
        return f"{self.customer_name} - Table {self.table.table_num}"

    def clean(self):
        # Check if the table is already booked at the same time
        conflicting_bookings = Booking.objects.filter(
            table=self.table,
            reservation_time=self.reservation_time,
        )
        if self.pk:
            conflicting_bookings = conflicting_bookings.exclude(pk=self.pk)
        if conflicting_bookings.exists():
            raise ValidationError("This table is already booked at the selected time.")















