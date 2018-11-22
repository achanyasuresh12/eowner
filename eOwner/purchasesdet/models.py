from django.db import models


class Purchasesdetails(models.Model):
    itemname = models.CharField(max_length=20, default='')
    itemquantity = models.CharField(max_length=20, default='')
    itembasicrate = models.CharField(max_length=20, default='')
    itemunittotal = models.CharField(max_length=20, default='')
    purchaseinvoice = models.BigIntegerField()

    def __str__(self):
        return self.itemname
