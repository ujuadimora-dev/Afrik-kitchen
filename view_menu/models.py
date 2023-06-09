from django.db import models
from django.contrib.auth.models import User


# Choice fields
ITEM_TYPES = (
    ("breakfast", "Breakfast"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
    ("drink", "Drink"),
    ("side", "Side")
)


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


class Menu(models.Model):
    """ Model to create Menu"""
    name = models.CharField(max_length=45)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    breakfasts = models.ManyToManyField('FoodMenu', related_name='breafasts')
    lunchs = models.ManyToManyField('FoodMenu', related_name='lunchs')
    dinners = models.ManyToManyField('FoodMenu', related_name='dinners')
    drinks = models.ManyToManyField('FoodMenu', related_name='drinks')
    sides = models.ManyToManyField('FoodMenu', related_name='sides')


class Meta:
    """order by active and name"""
    ordering = ['-active', 'name']


def __str__ (self):
    return str(self.name)
