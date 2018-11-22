from django import forms
from . import models


class purchases_forms(forms.ModelForm):

    class Meta:
        model = models.Purchases
        fields = ['purchaseinvoice', 'purchasedate']



