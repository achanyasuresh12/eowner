from django.shortcuts import render, redirect
from busdetails.models import Busdetails


def buss(request):

    model_object1 = Busdetails.objects.all()

    return render(request, "viewbusdetails/viewbusdetails.html", {'data': model_object1})

