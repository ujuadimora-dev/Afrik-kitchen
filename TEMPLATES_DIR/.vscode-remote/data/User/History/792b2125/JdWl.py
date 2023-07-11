from django import forms
from .models import Breakfast, Lunch, Dinner, Sides

from django import forms

MENU_CHOICES = [
    ('BREAKFAST', 'Breakfast'),
    ('LUNCH', 'Lunch'),
    ('DINNER', 'Dinner'),
    ('SIDE', 'Side'),
]


class MenuForm(forms.Form):
    menu_type = forms.ChoiceField(
        choices=MENU_CHOICES,
        widget=forms.RadioSelect
    )
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    name = forms.CharField(max_length=100)
    priceM = forms.DecimalField(max_digits=6, decimal_places=2)
    priceL = forms.DecimalField(max_digits=6, decimal_places=2)
    vegetarian = forms.BooleanField(required=False)
    calorie_count = forms.IntegerField()


class MenuCreateForm(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(),
            MenuForm(),
        )
        super().__init__(fields, *args, **kwargs)
        self.widget = MenuCreateWidget(widgets=[field.widget for field in self.fields])

    def compress(self, data_list):
        if data_list:
            return {
                'menu_type': data_list[0],
                'menu_details': data_list[1],
            }
        return {}


class MenuCreateWidget(forms.MultiWidget):
    def __init__(self, attrs=None, widgets=None):
        widgets = widgets or [forms.TextInput(), forms.HiddenInput()]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value['menu_type'], value['menu_details']]
        return [None, None]
