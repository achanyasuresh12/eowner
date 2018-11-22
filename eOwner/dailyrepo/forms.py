from django import forms
from . import models


class dailyreports_forms(forms.ModelForm):

    class Meta:
        model = models.Dailyreports
        fields = ["bus_id", "date", "totalcollection", "wages", "fuel_quantity", "fuel_price", "company", "address", "phone", "extra_charge", "tyre_charge", "spare_parts", "other_expenses", "staff_det"]
