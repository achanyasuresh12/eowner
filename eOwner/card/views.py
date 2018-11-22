from django.shortcuts import render, redirect


def cards(request):

    return render(request, "payment/Payment/CardPayment.html")

