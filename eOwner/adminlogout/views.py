from django.shortcuts import render, redirect


def adlogout(request):
    return render(request, "login/login.html")

