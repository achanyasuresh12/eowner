from django.db import models


class Branchdetails(models.Model):
    name = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    district = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=20, default='')
    contact = models.IntegerField()
    type = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name


