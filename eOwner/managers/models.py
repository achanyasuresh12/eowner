from datetime import date

from django.db import models
from datetime import date
CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))


class Managers(models.Model):
    mgrname = models.CharField(max_length=20, default='')
    mgrhouse = models.CharField(max_length=20, default='')
    mgrplace = models.CharField(max_length=20, default='')
    mgrcity = models.CharField(max_length=20, default='')
    mgremail = models.EmailField()
    mgrgender = models.CharField(choices=CHOICES, max_length=10)
    mgrdob = models.DateField(default=date.today)
    mgrcontact = models.CharField(max_length=10, default='')
    mgrusername = models.CharField(max_length=20, default='')
    mgrpassword = models.CharField(max_length=20, default='')
    mgrdate_of_join = models.DateField(default=date.today)
    mgrqualification = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.mgrname
