from django.shortcuts import render, redirect


def nets(request):

    return render(request, "payment/Payment/NetBanking.html")

