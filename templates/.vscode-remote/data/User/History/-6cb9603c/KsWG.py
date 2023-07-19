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
        widget=forms.RadioSelect,
        error_messages={
            'required': 'Please select a menu type.',
        }
    )
    
    description = forms.CharField(widget=forms.Textarea)
    fimage = forms.URLField()
    name = forms.CharField(max_length=100)
    priceM = forms.DecimalField(max_digits=6, decimal_places=2)
    priceL = forms.DecimalField(max_digits=6, decimal_places=2)
    vegetarian = forms.BooleanField(required=False)
    calorie_count = forms.IntegerField()
    created_on = forms.DateField()
    created_by_staff = forms.CharField(max_length=25)

    def save(self):
        """ Process the form data"""
        menu_type = self.cleaned_data['menu_type']

        if menu_type == 'BREAKFAST':
            return BreakFast.objects.create(**self.cleaned_data)

        elif menu_type == 'LUNCH':
            return Lunch.objects.create(**self.cleaned_data)

        elif menu_type == 'DINNER':
            return Dinner.objects.create(**self.cleaned_data)

        elif menu_type == 'SIDE':
            return Sides.objects.create(**self.cleaned_data)

        return None


class MenuCreateForm(BaseMenuForm):
    created_on = forms.DateField()
    created_by_staff = forms.CharField(max_length=25)





        










    