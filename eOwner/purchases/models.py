from datetime import date

from django.db import models


class Purchases(models.Model):
    purchaseinvoice = models.CharField(max_length=20, default='')
    purchasedate = models.DateField(default=date.today)
    purchasegrandtotal = models.CharField(max_length=20, default='')
    mgr_id = models.BigIntegerField()

    def __str__(self):
        return self.purchaseinvoice



