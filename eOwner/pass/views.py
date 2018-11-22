from django.shortcuts import render
# Create your views here.


def passhome(request):
    return render(request, 'pass/pass.html')
