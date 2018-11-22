from django.shortcuts import render, redirect


def payments(request):

    return render(request, "payment/Payment/PaymentMethod.html")

