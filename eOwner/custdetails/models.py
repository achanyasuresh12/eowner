from django.db import models
CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))


class Cust(models.Model):
    custname = models.CharField(max_length=20, default='')
    custage = models.CharField(max_length=20, default='')
    custgender = models.CharField(choices=CHOICES, max_length=10)
    custemail = models.EmailField()
    custcontact = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.custname

