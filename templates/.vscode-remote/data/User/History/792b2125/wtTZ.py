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
    #fimage = forms.ImageField()
    fimage = forms.URLField()
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
    description = forms.CharField(widget=forms.Textarea)
    fimage = forms.URLField()
    #image = forms.ImageField()
    name = forms.CharField(max_length=100)
    priceM = forms.DecimalField(max_digits=5, decimal_places=2)
    priceL = forms.DecimalField(max_digits=5, decimal_places=2)
    vegetarian = forms.BooleanField(required=False)
    calorie_count = forms.IntegerField()
    created_on = models.DateField()
    created_by_staff = models.TextField(max_length=25)

    def save(self):
        # Process the form data
        menu_type = self.cleaned_data['menu_type']
        
        if menu_type == 'BREAKFAST':
            breakfast = BreakFast.objects.create(
                description=self.cleaned_data['description'],
                fimage=self.cleaned_data['fimage'],
                name=self.cleaned_data['name'],
                priceM=self.cleaned_data['priceM'],
                priceL=self.cleaned_data['priceL'],
                vegetarian=self.cleaned_data['vegetarian'],
                calorie_count=self.cleaned_data['calorie_count']
                created_on=self.cleaned_data['created_on'],
                created_by_staff = models.TextField(max_length=25)
            )
            # Additional processing if needed
            
        elif menu_type == 'LUNCH':
            lunch = Lunch.objects.create(
                description=self.cleaned_data['description'],
                fimage=self.cleaned_data['fimage'],
                name=self.cleaned_data['name'],
                priceM=self.cleaned_data['priceM'],
                priceL=self.cleaned_data['priceL'],
                vegetarian=self.cleaned_data['vegetarian'],
                calorie_count=self.cleaned_data['calorie_count']
            )
            # Additional processing if needed
            
        elif menu_type == 'DINNER':
            dinner = Dinner.objects.create(
                description=self.cleaned_data['description'],
                fimage=self.cleaned_data['fimage'],
                name=self.cleaned_data['name'],
                priceM=self.cleaned_data['priceM'],
                priceL=self.cleaned_data['priceL'],
                vegetarian=self.cleaned_data['vegetarian'],
                calorie_count=self.cleaned_data['calorie_count']
            )
            # Additional processing if needed
            
        elif menu_type == 'SIDE':
            sides = Sides.objects.create(
                description=self.cleaned_data['description'],
                fimage=self.cleaned_data['fimage'],
                name=self.cleaned_data['name'],
                priceM=self.cleaned_data['priceM'],
                priceL=self.cleaned_data['priceL'],
                vegetarian=self.cleaned_data['vegetarian'],
                calorie_count=self.cleaned_data['calorie_count']
            )
            # Additional processing if needed
