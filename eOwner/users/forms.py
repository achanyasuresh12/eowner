from django import forms
from . import models


class user_forms(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ['psgname', 'psgage', 'psggender', 'psgemail', 'psgcontact', 'psgusername', 'psgpassword']

