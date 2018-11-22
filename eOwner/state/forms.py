from django import forms
from . import models


class state_forms(forms.ModelForm):

    class Meta:
        model = models.State
        fields = ["state_name"]
