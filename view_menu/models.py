from django.db import models
from django.contrib.auth.models import User




class FoodMenu(models.Model):
    """ Model to create the menu list"""
    name = models.CharField(max_length=45)
    description = models.TextField()
    price = models.FloatField(default=0.00)
    image = models.ImageField(upload_to='media/',blank=True, null=True)


class Meta:
    """ Order by name"""
    ordering = ['name']

def __str__ (self):
    return str(self.name)