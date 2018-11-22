from django import forms
from . import models


class seatinform_forms(forms.ModelForm):

    class Meta:
        model = models.SeatDet
        fields = ["bus_id", "Seat_name", "rate"]
