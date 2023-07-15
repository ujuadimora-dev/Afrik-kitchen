from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

MENU_CHOICES = [
    ('BREAKFAST', 'Breakfast'),
    ('LUNCH', 'Lunch'),
    ('DINNER', 'Dinner'),
    ('SIDE', 'Side'),
]


class MenuItem(models.Model):
    fimage = models.URLField()
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=25, choices=MENU_CHOICES, default='breakfast'
    )
    description = models.TextField(default='food_description')
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    vegetarian = models.BooleanField(default=False)
    calorie_count = models.IntegerField(default=0)
    created_on = models.DateField(default=timezone.now)
    created_by_staff = models.CharField(max_length=25, default='staff')

    objects = models.Manager()

    class Meta:
        """ Order by type and name """
        ordering = ['type', 'name']

    def __str__(self):
        return str(self.name)



# class BreakFast(MenuItem):
#     pass


# class Lunch(MenuItem):
#     pass


# class Dinner(MenuItem):
#     pass


# class Sides(MenuItem):
#     pass



class Menu(models.Model):
    """ Model to create a menu """
    name = models.CharField(max_length=25)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    breakfasts = models.ManyToManyField('MenuItem', related_name='breakfasts')
    lunchs = models.ManyToManyField('MenuItem', related_name='lunchs')
    dinners = models.ManyToManyField('MenuItem', related_name='dinners')
    sides = models.ManyToManyField('MenuItem', related_name='sides')
    sides = models.ManyToManyField('MenuItem', related_name='sides')

    class Meta:
        """ Order by active and name """
        ordering = ['-active', 'name']

    def __str__(self):
        return str(self.name)
