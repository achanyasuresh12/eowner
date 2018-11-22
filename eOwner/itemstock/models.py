from django.db import models


class Itemstock(models.Model):
    name = models.CharField(max_length=20, default='')
    quantity = models.IntegerField()
    purchasedate = models.DateField()
    renewaldate = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
