from datetime import date


from django.db import models


class Bookbus(models.Model):

    source = models.CharField(max_length=30, default='')
    destination = models.CharField(max_length=30, default='')
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.source

