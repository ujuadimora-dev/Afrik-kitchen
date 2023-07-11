from django import forms

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
    
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    name = forms.CharField(max_length=100)
    priceM = forms.DecimalField(max_digits=6, decimal_places=2)
    priceL = forms.DecimalField(max_digits=6, decimal_places=2)
    vegetarian = forms.BooleanField(required=False)
    calorie_count = forms.IntegerField()


class MenuCreateForm(forms.Form):
    menu_type = forms.ChoiceField(
        choices=MENU_CHOICES,
        widget=forms.RadioSelect,
        error_messages={
            'required': 'Please select a menu type.',
        }
    )
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    name = forms.CharField(max_length=100)
    priceM = forms.DecimalField(max_digits=6, decimal_places=2)
    priceL = forms.DecimalField(max_digits=6, decimal_places=2)
    vegetarian = forms.BooleanField(required=False)
    calorie_count = forms.IntegerField()

    def save(self):
        # Process the form data
        menu_type = self.cleaned_data['menu_type']
        
        if menu_type == 'BREAKFAST':
            breakfast = Breakfast.objects.create(
                content=self.cleaned_data['content'],
                image=self.cleaned_data['image'],
                name=self.cleaned_data['name'],
                priceM=self.cleaned_data['priceM'],
                priceL=self.cleaned_data['priceL'],
                vegetarian=self.cleaned_data['vegetarian'],
                calorie_count=self.cleaned_data['calorie_count']
            )
            # Additional processing if needed
            
        elif menu_type == 'LUNCH':
            lunch = Lunch.objects.create(
                content=self.cleaned_data['content'],
                image=self.cleaned_data['image'],
                name=self.cleaned_data['name'],
                priceM=self.cleaned_data['priceM'],
                priceL=self.cleaned_data['priceL'],
                vegetarian=self.cleaned_data['vegetarian'],
                calorie_count=self.cleaned_data['calorie_count']
            )
            # Additional processing if needed
            
        elif menu_type == 'DINNER':
            dinner = Dinner.objects.create(
                content=self.cleaned_data['content'],
                image=self.cleaned_data['image'],
                name=self.cleaned_data['name'],
                priceM=self.cleaned_data['priceM'],
                priceL=self.cleaned_data['priceL'],
                vegetarian=self.cleaned_data['vegetarian'],
                calorie_count=self.cleaned_data['calorie_count']
            )
            # Additional processing if needed
            
        elif menu_type == 'SIDE':
            sides = Sides.objects.create(
                content=self.cleaned_data['content'],
                image=self.cleaned_data['image'],
                name=self.cleaned_data['name'],
                priceM=self.cleaned_data['priceM'],
                priceL=self.cleaned_data['priceL'],
                vegetarian=self.cleaned_data['vegetarian'],
                calorie_count=self.cleaned_data['calorie_count']
            )
            # Additional processing if needed
