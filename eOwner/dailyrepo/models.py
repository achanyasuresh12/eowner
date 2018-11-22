from datetime import date

from django.db import models
from busdetails .models import Busdetails
from managers .models import Managers
from stafftype .models import Stafftype


class Dailyreports(models.Model):
    bus_id = models.ForeignKey(Busdetails, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    totalcollection = models.BigIntegerField()
    wages = models.BigIntegerField()
    fuel_quantity = models.IntegerField()
    fuel_price = models.BigIntegerField()
    fuel_total = models.BigIntegerField()
    company = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=20, default='')
    phone = models.BigIntegerField()
    extra_charge = models.BigIntegerField()
    tyre_charge = models.BigIntegerField()
    spare_parts = models.BigIntegerField()
    other_expenses = models.BigIntegerField()
    net_balance = models.BigIntegerField()
    staff_det = models.ForeignKey(Stafftype, on_delete=models.CASCADE)
    mgr_id = models.BigIntegerField()

    def __str__(self):
        return self.totalcollection
