from django import forms
from . import models


class user_forms(forms.ModelForm):
    custname = forms.CharField(
        required=True,
        label='custname',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'Enter character only'})
    )

    custage = forms.IntegerField(
        required=True,
        label='custage',
        widget=forms.TextInput(attrs={'pattern': '[0-9]+', 'title': 'Enter Number only'})
    )
    custcontact = forms.IntegerField(
        required=True,
        label='custcontact',
        widget=forms.TextInput(attrs={'pattern': '[0-9]+', 'title': 'Enter Number only'})
    )
    class Meta:
        model = models.Cust
        fields = ['custname', 'custage', 'custgender', 'custemail', 'custcontact']

