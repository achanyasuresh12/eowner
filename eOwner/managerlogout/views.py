from django.shortcuts import render, redirect


def mglogout(request):
    return render(request, "managerloginpage/managerlogin.html")

