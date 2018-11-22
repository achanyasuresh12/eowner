from django import forms
from . import models


class manager_forms(forms.ModelForm):
    mgrname = forms.CharField(
        required=True,
        label='managername',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'Enter character only'})
    )

    mgrhouse = forms.CharField(
        required=True,
        label='managerhouse',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'Enter character only'})
    )
    mgrplace = forms.CharField(
        required=True,
        label='managerplace',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'Enter character only'})
    )
    mgrcity = forms.CharField(
        required=True,
        label='managercity',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'Enter character only'})
    )
    mgrcontact = forms.IntegerField(
        required=True,
        label='managercontact',
        widget=forms.TextInput(attrs={'pattern': '[0-9]+', 'title': 'Enter Number only'})

    )



    class Meta:
        model = models.Managers
        fields = ['mgrname', 'mgrhouse', 'mgrplace', 'mgrcity', 'mgremail', 'mgrgender', 'mgrdob', 'mgrcontact', 'mgrusername', 'mgrpassword', 'mgrdate_of_join', 'mgrqualification']
