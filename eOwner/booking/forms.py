from django import forms
from . import models


class booking_forms(forms.ModelForm):

    class Meta:
        model = models.Ticketbooking
        fields = ["date", "source", "destination", "seat", "bus_id", "duration", "dropping_points", "fare"]
