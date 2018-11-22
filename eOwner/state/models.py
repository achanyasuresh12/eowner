from django.db import models
from managers .models import Managers


class State(models.Model):
    state_name = models.CharField(max_length=30, default='')
    mgr_id = models.BigIntegerField()

    def __str__(self):
        return self.state_name
