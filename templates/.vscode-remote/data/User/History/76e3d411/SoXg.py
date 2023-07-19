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

    


