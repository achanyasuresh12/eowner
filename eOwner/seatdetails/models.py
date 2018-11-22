from django.db import models
from busdetails .models import Busdetails


class SeatDet(models.Model):
    bus_id = models.ForeignKey(Busdetails, on_delete=models.CASCADE)
    Seat_name = models.CharField(max_length=20, default='')
    rate = models.CharField(max_length=20, default='')
    status = models.CharField(max_length=10, default=0)

    def __str__(self):
        return self.Seat_name
