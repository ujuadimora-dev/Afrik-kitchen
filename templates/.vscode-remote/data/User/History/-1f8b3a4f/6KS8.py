from django.db import models


class BreakFast(models.Model):
    name = models.CharField(max_length=100)
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    fimage = models.ImageField(upload_to='menu_images')  # Add this line

class Meta:
    """ Order by name"""
    ordering = ['name', '_created_on']

    def __str__ (self):
        return str(self.name)
    


   

   

