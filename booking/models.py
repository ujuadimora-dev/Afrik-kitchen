from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import models



# Choice of fields
CAPACITY = ((2, "2"), (3, "3"), (4, "4"), (8, "8"), (14, "14"))
BOOKING_TIME = (
    (1, "8:00am - 9:45am"),
    (2, "10:00am - 12:45pm"),
    (3, "1:00pm - 2:45pm"),
    (4, "3:00pm - 5:45pm"),
    (5, "7:00pm - 8:45pm")
)
TABLE_POSITION = (
    ("window", "Tables near the window"),
    ("middle", "Tables in the middle"),
    ("outside", "Tables outside in the garden"),
    ("corridor", "Tables on the corridor")
)


class CreateTable(models.Model):
    """This is to create the Table for booking"""
    table_num = models.IntegerField(default=0)
    capacity = models.IntegerField(choices=CAPACITY, default=2)
    table_position = models.CharField(max_length=10, choices=TABLE_POSITION, default='window')
    wheelchair_accessible = models.BooleanField(default=False)

    def __str__(self):
        return str(self.table_num)


class Booking(models.Model):
    """Model to create a booking"""
    
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=20, null=True)
    reservation_date_and_time = models.DateTimeField(null=True)
    booked_table = models.ForeignKey(
        CreateTable, on_delete=models.CASCADE, related_name="booking_table"
    )
    number_of_guests = models.IntegerField(default=2)
    reservation_date = models.DateField()
    reservation_time = models.IntegerField(choices=BOOKING_TIME, default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Order by reservation_date and then reservation_time"""
        ordering = ['reservation_date', 'reservation_time']

    def __str__(self):
        """
        Function to return object model
        items as string.
        """
        return f'User {self.user} has made a booking ' \
               f'for {self.customer_name} ' \
               f'for {self.number_of_guests} guest(s) ' \
               f'at {self.booked_table.table_position} ' \
               f'on {self.reservation_date} ' \
               f'at {next(time for time, _ in BOOKING_TIME if time == self.reservation_time)}.'



class ManageBooking(models.Model):
    @staticmethod
    def cancel_booking(booking_id):
        try:
            booking = Booking.objects.get(id=booking_id)
            booking.delete()
            return True
        except Booking.DoesNotExist:
            return False

    @staticmethod
    def delete_booking(booking_id):
        try:
            booking = Booking.objects.get(id=booking_id)
            booking.delete()
            return True
        except Booking.DoesNotExist:
            return False

    @staticmethod
    def update_booking(booking_id, new_data):
        try:
            booking = Booking.objects.get(id=booking_id)
            for key, value in new_data.items():
                setattr(booking, key, value)
            booking.save()
            return True
        except Booking.DoesNotExist:
            return False

    @staticmethod
    def get_bookings_by_date(date):
        bookings = Booking.objects.filter(reservation_date=date)
        return bookings

    @staticmethod
    def get_bookings_by_customer(customer_name):
        bookings = Booking.objects.filter(
            Q(user__username=customer_name) | Q(customer_name=customer_name)
        )
        return bookings
