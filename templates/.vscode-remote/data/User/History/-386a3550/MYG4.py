from django.db import models


class BreakFast(models.Model):
    fimage = models.URLField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    vegetarian = forms.BooleanField(required=False)
    calorie_count = forms.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Lunch(models.Model):
    fimage = models.URLField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    vegetarian = forms.BooleanField(required=False)
    calorie_count = forms.IntegerField()
    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Dinner(models.Model):
    fimage = models.URLField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    vegetarian = forms.BooleanField(required=False)
    calorie_count = forms.IntegerField()
    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Sides(models.Model):
    fimage = models.URLField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    vegetarian = forms.BooleanField(required=False)
    calorie_count = forms.IntegerField()
    created_on = models.DateField()
   

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)
