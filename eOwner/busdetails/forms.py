from django import forms
from . import models


class busdetails_forms(forms.ModelForm):

    class Meta:
        model = models.Busdetails
        fields = ["name", "regno", "permitno", "seat", "source", "destination", "description", "arrival_time", "departure_time", "seatorder"]
