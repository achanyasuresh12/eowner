from datetime import date

from django.db import models
from datetime import date
CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))


class Employee(models.Model):
    empname = models.CharField(max_length=20, default='')
    emphouse = models.CharField(max_length=20, default='')
    empplace = models.CharField(max_length=20, default='')
    empcity = models.CharField(max_length=20, default='')
    empemail = models.EmailField()
    empgender = models.CharField(choices=CHOICES, max_length=10)
    empdob = models.DateField(default=date.today)
    empcontact = models.CharField(max_length=5, default='')
    empdate_of_join = models.DateField(default=date.today)
    empqualification = models.CharField(max_length=20, default='')
    emp_licence_number = models.IntegerField()
    licence_validity = models.DateField(default=date.today)

    def __str__(self):
        return self.empname
