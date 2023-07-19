from django.db import models
from django.utils import timezone



class MenuItem(models.Model):
    """ Model to create Menu Items """
    fimage = models.URLField()
    name = models.CharField(max_length=100)
    description = models.TextField(default='Unknown')
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    vegetarian = models.BooleanField(default=False)
    calorie_count = models.IntegerField(default=0)
    created_on = models.DateField(default=timezone.now)
    created_by_staff = models.CharField(max_length=25, default='Unknown')


    class Meta:
        abstract = True
        ordering = ['name']

        def __str__(self):
            return str(self.name)


class BreakFast(MenuItem):
    pass


class Lunch(MenuItem):
    pass


class Dinner(MenuItem):
    pass


class Sides(MenuItem):
    pass









