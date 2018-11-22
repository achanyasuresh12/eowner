from django.shortcuts import render, redirect
from seatdetails.models import SeatDet
from django.db import connection


def viewseat(request):

    model_object1 = SeatDet.objects.all()

    return render(request, "viewseatdet/viewseatdet.html", {'data': model_object1})


def verify_details(request, pk):
    cursor = connection.cursor()
    cursor.execute("update seatdetails_seatdet set status='Booked' where id='%s'" % (pk,))
    return redirect('custdetails:custdetails_forms')
