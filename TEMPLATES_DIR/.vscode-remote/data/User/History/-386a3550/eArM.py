from django.db import models


class BreakFast(models.Model):
    name = models.CharField(max_length=100)
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    fimage = models.URLField()

    class Meta:
        """ Order by name"""
        ordering = ['name', '_created_on']

    def __str__(self):
        return str(self.name)


class Lunch(models.Model):
    name = models.CharField(max_length=100)
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    fimage = models.URLField()

    class Meta:
        """ Order by name"""
        ordering = ['name', '_created_on']

    def __str__(self):
        return str(self.name)


class Dinner(models.Model):
    name = models.CharField(max_length=100)
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    fimage = models.URLField()

    class Meta:
        """ Order by name"""
        ordering = ['name', '_created_on']

    def __str__(self):
        return str(self.name)


class Sides(models.Model):
    name = models.CharField(max_length=100)
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    fimage = models.URLField()

    class Meta:
        """ Order by name"""
        ordering = ['name', '_created_on']

    def __str__(self):
        return str(self.name)
