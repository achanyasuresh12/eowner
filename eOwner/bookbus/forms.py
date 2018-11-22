from django import forms
from . import models


class bookbus_forms(forms.ModelForm):

    class Meta:
        model = models.Bookbus
        fields = ["source", "destination", "date"]

