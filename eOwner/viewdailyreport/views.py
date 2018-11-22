from django.shortcuts import render, redirect
from dailyrepo.models import Dailyreports


def report(request):
    model_object1 = Dailyreports.objects.all()

    return render(request, "viewdailyreport/viewdailyreport.html", {'data': model_object1})

