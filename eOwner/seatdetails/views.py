from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import SeatDet


def seatde(request):
    if request.method == 'POST':
        form = forms.seatinform_forms(request.POST, request.FILES)
        if form.is_valid():
            seatObj = form.cleaned_data
            bus_id = seatObj['bus_id']
            seat_name = seatObj['seat_name']
            rate = seatObj['rate']
            status = seatObj['status']
            a = SeatDet(bus_id=bus_id, seat_name=seat_name, rate=rate, status=status)
            a.save()
            return redirect('seatdetails:seatinform_forms')
    else:
        form = forms.seatinform_forms

    return render(request, "seatinfo/seatinfo.html")
