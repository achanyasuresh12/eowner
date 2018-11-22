from django.db import models
from busdetails . models import Busdetails
from managers . models import Managers


class Businfo(models.Model):
    name = models.ForeignKey(Busdetails, on_delete=models.CASCADE)
    dropping_points = models.CharField(max_length=20, default='')
    mgr_id = models.BigIntegerField()

    def __str__(self):
        return self.name


