from django.shortcuts import render, redirect
from busdetails.models import Busdetails


def busses(request):

    model_object1 = Busdetails.objects.all()

    return render(request, "busview/busview.html", {'data': model_object1})

