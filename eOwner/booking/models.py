from datetime import date

from django.db import models
from busdetails .models import Busdetails
from users .models import User


class Ticketbooking(models.Model):
    date = models.DateField(default=date.today)
    source = models.CharField(max_length=20, default='')
    destination = models.CharField(max_length=20, default='')
    seat = models.IntegerField()
    bus_id = models.ForeignKey(Busdetails, on_delete=models.CASCADE)
    duration = models.CharField(max_length=20, default='')
    dropping_points = models.CharField(max_length=20, default='')
    fare = models.CharField(max_length=20, default='')
    user_id = models.BigIntegerField()

    def __str__(self):
        return self.source
