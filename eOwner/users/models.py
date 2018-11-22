from django.db import models
CHOICES = (('male', 'male'), ('female', 'female'), ('others', 'others'))


class User(models.Model):
    psgname = models.CharField(max_length=20, default='')
    psgage = models.CharField(max_length=20, default='')
    psggender = models.CharField(choices=CHOICES, max_length=10)
    psgemail = models.CharField(max_length=30, default='')
    psgcontact = models.CharField(max_length=20, default='')
    psgusername = models.CharField(max_length=20, default='')
    psgpassword = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.psgname

