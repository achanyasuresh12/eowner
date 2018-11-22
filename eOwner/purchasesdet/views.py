from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Purchasesdetails
from purchases.models import Purchases


def purchasesdetails(request):

    purchaseinvoice = request.session['purchaseinvoice']
    pkphobj = Purchases.objects.get(purchaseinvoice=purchaseinvoice)
    fk = pkphobj.id
    #request.session[purchaseinvoice] = pk
    model_object = Purchasesdetails.objects.filter(purchaseinvoice=fk)

    if request.method == 'POST':
        form = forms.purchasesdetails_forms(request.POST, request.FILES)
        if form.is_valid():
            purObj = form.cleaned_data
            itemname = purObj['itemname']
            itemquantity = purObj['itemquantity']
            itembasicrate = purObj['itembasicrate']
            total = int(itembasicrate)*int(itemquantity)

            a = Purchasesdetails(itemname=itemname, itemquantity=itemquantity, itembasicrate=itembasicrate, itemunittotal=total, purchaseinvoice=fk)
            a.save()

            return redirect('purchasesdet:purchasesdetails_forms')
    else:
        form = forms.purchasesdetails_forms

    return render(request, "purchasedet/purchasedetails.html", {'form': form, 'data': model_object, 'invs': purchaseinvoice})
