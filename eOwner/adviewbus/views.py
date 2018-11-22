from django.shortcuts import render, redirect
from busdetails.models import Busdetails


def admbus(request):

    model_object1 = Busdetails.objects.all()

    return render(request, "adminviewbus/adminviewbus.html", {'data': model_object1})

