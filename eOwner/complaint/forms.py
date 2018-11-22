from django import forms
from . import models


class complaint_forms(forms.ModelForm):

    class Meta:
        model = models.Complaint
        fields = ["complaintcontent", "bus_id"]
