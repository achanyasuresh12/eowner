from django.db import models
from users.models import User
from busdetails.models import Busdetails


class Feedback(models.Model):
    feedbackcontent = models.CharField(max_length=50, default='')
    bus_id = models.ForeignKey(Busdetails, on_delete=models.CASCADE)
    user_id = models.BigIntegerField()

    def __str__(self):
        return self.feedbackcontent

