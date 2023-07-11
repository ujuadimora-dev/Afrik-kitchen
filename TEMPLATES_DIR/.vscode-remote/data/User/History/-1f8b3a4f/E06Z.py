from django.db import models

# Create your models here.

class MenuPrice(models.Model):
    name = models.CharField(max_length=45)
    priceM = models.DecimalField(max_digits=4, decemal_places=2)
    priceL = models.DecimalField(max_digits=4, decemal_places=2)
    Pimage = models.URLField()