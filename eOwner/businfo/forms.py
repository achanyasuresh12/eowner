from django import forms
from . import models


class businfo_forms(forms.ModelForm):

    class Meta:
        model = models.Businfo
        fields = ["name", "dropping_points"]
