from django import forms
from .models import Breakfast, Lunch, Dinner, Sides

MENU_CHOICES = [
    ("BREAKFAST", "Breakfast"),
    ("LUNCH", "Lunch"),
    ("DINNER", "Dinner"),
    ("SIDE", "Side"),
]

class MenuForm(forms.ModelForm):
    menu_type = forms.ChoiceField(
        choices=MENU_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = MenuForm
        fields = ['menu_type', 'content', 'image', 'name', 'priceM', 'priceL', 'vegetarian', 'calorie_count']


class BreakfastForm(forms.ModelForm):
    class Meta:
        model = Breakfast
        fields = ['content', 'image', 'name', 'priceM', 'priceL', 'vegetarian', 'calorie_count']


class LunchForm(forms.ModelForm):
    class Meta:
        model = Lunch
        fields = ['content', 'image', 'name', 'priceM', 'priceL', 'vegetarian', 'calorie_count']


class DinnerForm(forms.ModelForm):
    class Meta:
        model = Dinner
        fields = ['content', 'image', 'name', 'priceM', 'priceL', 'vegetarian', 'calorie_count']


class SidesForm(forms.ModelForm):
    class Meta:
        model = Sides
        fields = ['content', 'image', 'name', 'priceM', 'priceL', 'vegetarian', 'calorie_count']
