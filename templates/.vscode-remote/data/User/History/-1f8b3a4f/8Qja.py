from django.db import models

class MenuPrice(models.Model):
    name = models.CharField(max_length=45)
    priceM = models.DecimalField(max_digits=4, decimal_places=2)
    priceL = models.DecimalField(max_digits=4, decimal_places=2)
    Pimage = models.URLField()
