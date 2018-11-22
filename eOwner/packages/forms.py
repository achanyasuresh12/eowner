from django import forms
from . import models


class packages_forms(forms.ModelForm):

    class Meta:
        model = models.Packages
        fields = ["name", "duration", "seatcount", "rate", "description"]
