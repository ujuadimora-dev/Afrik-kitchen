from django.db import models
import datetime






class BreakFast(models.Model):
    fimage = models.URLField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    vegetarian = models.BooleanField(default=False)
    calorie_count = models.IntegerField(default=0)
    created_on = models.DateField(default=datetime.date.today)
    created_by_staff = models.CharField(max_length=25, default='Unknown')


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
    vegetarian = models.BooleanField()
    calorie_count = models.IntegerField()
    created_on = models.DateField()
    created_by_staff = models.TextField(max_length=25)
    

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
    vegetarian = models.BooleanField()
    calorie_count = models.IntegerField()
    created_on = models.DateField()
    created_by_staff = models.TextField(max_length=25)
    

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
    vegetarian = models.BooleanField()
    calorie_count = models.IntegerField()
    created_on = models.DateField()
    created_by_staff = models.TextField(max_length=25)
   

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)
