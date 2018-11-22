import datetime


from django.shortcuts import render, redirect
from . import forms
from .models import Purchases


def purchase(request):
    login_id = request.session['logid']
    model_object = Purchases.objects.filter(mgr_id=login_id)

    if request.method == 'POST':

        form = forms.purchases_forms(request.POST, request.FILES)
        if form.is_valid():
            purchaseObj = form.cleaned_data
            purchaseinvoice = purchaseObj['purchaseinvoice']
            purchasedate = purchaseObj['purchasedate']
            request.session['purchaseinvoice'] = purchaseinvoice

            a = Purchases(purchaseinvoice=purchaseinvoice, purchasedate=purchasedate, mgr_id=login_id)
            a.save()

            return redirect('purchases:purchases_forms')
    else:
        form = forms.purchases_forms

    return render(request, "purchase/purchasedetails1.html", {'form': form, 'data': model_object})
