from django import forms
from . import models

class purchasesdetails_forms(forms.ModelForm):

   class Meta:
    model = models.Purchasesdetails
    fields = ['itemname', 'itemquantity', 'itembasicrate']

