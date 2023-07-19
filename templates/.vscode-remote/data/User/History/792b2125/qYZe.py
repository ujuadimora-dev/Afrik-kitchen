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


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["name", "title", "birth_date"]


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "authors"]


breakfast  = 'BreakFast'


