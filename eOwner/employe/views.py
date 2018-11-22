from django.shortcuts import render, redirect
from . import forms
from .models import Employee


def emp(request):

    if request.method == 'POST':
        form = forms.emp_forms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return redirect('employe:emp_forms')
    else:
        form = forms.emp_forms

    return render(request, "employes/employes.html", {'form': form})

