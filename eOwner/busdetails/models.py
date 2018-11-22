from django.db import models
from managers . models import Managers


class Busdetails(models.Model):
    name = models.CharField(max_length=20, default='')
    regno = models.CharField(max_length=20, default='')
    permitno = models.CharField(max_length=20, default='')
    seat = models.IntegerField()
    source = models.CharField(max_length=30, default='')
    destination = models.CharField(max_length=30, default='')
    description = models .CharField(max_length=40, default='')
    arrival_time = models.CharField(max_length=20, default='')
    departure_time = models.CharField(max_length=20, default='')
    seatorder = models.CharField(max_length=20, default='')
    mgr_id = models.BigIntegerField()

    def __str__(self):
        return self.regno

