from django.shortcuts import render, redirect


def menus(request):

    return render(request, "menu/menu.html")

