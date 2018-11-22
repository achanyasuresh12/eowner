from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Dailyreports


def dailyrep(request):
    login_id = request.session['logid']
    model_object = Dailyreports.objects.filter(mgr_id=login_id)

    if request.method == 'POST':
        form = forms.dailyreports_forms(request.POST, request.FILES)
        if form.is_valid():
            repObj = form.cleaned_data
            bus_id = repObj['bus_id']
            date = repObj['date']
            totalcollection = repObj['totalcollection']
            wages = repObj['wages']
            fuel_quantity = repObj['fuel_quantity']
            fuel_price = repObj['fuel_price']
            fuel_total = fuel_quantity * fuel_price
            company = repObj['company']
            address = repObj['address']
            phone = repObj['phone']
            extra_charge = repObj['extra_charge']
            tyre_charge = repObj['tyre_charge']
            spare_parts = repObj['spare_parts']
            other_expenses = repObj['other_expenses']
            net_balance = totalcollection - (wages+fuel_total+extra_charge+tyre_charge+spare_parts+other_expenses)

            staff_det = repObj['staff_det']

            a = Dailyreports(bus_id=bus_id, date=date, totalcollection=totalcollection, wages=wages, fuel_quantity=fuel_quantity, fuel_price=fuel_price, fuel_total=fuel_total, company=company, address=address, phone=phone, extra_charge=extra_charge, tyre_charge=tyre_charge, spare_parts=spare_parts, other_expenses=other_expenses, net_balance=net_balance, staff_det=staff_det, mgr_id=login_id)
            a.save()
            return redirect('dailyrepo:dailyreports_forms')
    else:
        form = forms.dailyreports_forms

    return render(request, "dailyreport/dailyreport.html", {'form': form, 'data': model_object})


def edit_dailyrep(request, pk):
    login_id = request.session['logid']
    model_objects = Dailyreports.objects.filter(mgr_id=login_id)
    template = 'dailyreport/dailyreport.html'
    post = get_object_or_404(Dailyreports, pk=pk)

    if request.method == 'POST':
        form = forms.dailyreports_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('dailyrepo:dailyreports_forms')
    else:
        form = forms.dailyreports_forms(instance=post)
        context = {
                'form': form,
                'post': post,
                'data': model_objects,
            }
    return render(request, template, context)


def delete_dailyrep(request, pk):
    post = get_object_or_404(Dailyreports, pk=pk)
    post.delete()
    return redirect('dailyrepo:dailyreports_forms')
