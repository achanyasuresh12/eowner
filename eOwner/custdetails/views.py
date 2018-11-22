from django.shortcuts import render, redirect
from . import forms
from .models import Cust


def custo(request):

    if request.method == 'POST':
        form = forms.user_forms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return redirect('custdetails:custdetails_forms')
    else:
        form = forms.user_forms

    return render(request, "customer/customer.html", {'form': form})

