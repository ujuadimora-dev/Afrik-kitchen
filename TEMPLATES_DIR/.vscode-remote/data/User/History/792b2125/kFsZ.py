from django import forms
from .models import BreakFast, Lunch, Dinner, Sides
from django.db import models
from django.forms import ModelForm

MENu_CHOICES = [
("BREAKFAST", "BreakFast"),
("LUNCH", "Lunch."),
("DINNER", "Dinner."),
("SIDE", "Side."),
]


class MenuForm(models.Model):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    SIDES = 'Sides'
    
    def __str__(self):
        return self.name

    menu_type = forms.ChoiceField(
        choices=MENu_CHOICES,
        widget=forms.RadioSelect
    )
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    name = forms.CharField(max_length=100)
    priceM = forms.DecimalField(max_digits=6, decimal_places=2)
    priceL = forms.DecimalField(max_digits=6, decimal_places=2)
    vegetarian = forms.BooleanField(required=False)
    calorie_count = forms.IntegerField()


class Meta:
    


