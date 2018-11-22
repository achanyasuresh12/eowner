from django import forms
from . import models


class emp_forms(forms.ModelForm):
    empname = forms.CharField(
        required=True,
        label='empname',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'Enter character only'})
    )

    emphouse = forms.CharField(
        required=True,
        label='emphouse',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'Enter character only'})
    )
    empplace = forms.CharField(
        required=True,
        label='empplace',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'Enter character only'})
    )
    empcity = forms.CharField(
        required=True,
        label='empcity',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'Enter character only'})
    )
    empcontact = forms.IntegerField(
        required=True,
        label='empcontact',
        widget=forms.TextInput(attrs={'pattern': '[0-9]+', 'title': 'Enter Number only'})

    )

    class Meta:
        model = models.Employee
        fields = ['empemail', 'empgender', 'empdob', 'empcontact', 'empdate_of_join', 'empqualification', 'emp_licence_number', 'licence_validity']
