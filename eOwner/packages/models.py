from django.db import models
from managers .models import Managers


class Packages(models.Model):
    name = models.CharField(max_length=20, default='')
    duration = models.IntegerField()
    seatcount = models.IntegerField()
    rate = models.IntegerField()
    description = models.CharField(max_length=20, default='')
    mgr_id = models.BigIntegerField()

    def __str__(self):
        return self.name
