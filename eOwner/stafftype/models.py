from django.db import models


class Stafftype(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name
