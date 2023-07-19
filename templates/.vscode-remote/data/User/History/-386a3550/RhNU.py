from django.db import models


class BreakFast(models.Model):
    fimage = models.URLField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    fimage = models.URLField()

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
   
    vegetarian=self.cleaned_data['vegetarian'],
    calorie_count=self.cleaned_data['calorie_count']
    
    


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
    fimage = models.URLField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Sides(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    fimage = models.URLField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)
