from django.shortcuts import render, redirect
from . import forms
from .models import Bookbus


def bookbus(request):
    login_id = request.session['logid']
    model_object = Bookbus.objects.filter()

    if request.method == 'POST':
        form = forms.bookbus_forms(request.POST, request.FILES)
        if form.is_valid():
            bookObj = form.cleaned_data
            source = bookObj['source']
            destination = bookObj['destination']
            date = bookObj['date']
            a = Bookbus(source=source, destination=destination, date=date)
            a.save()
            return redirect('bookbus:bookbus_forms')
    else:
        form = forms.bookbus_forms

    return render(request, "bookbus/tours.html", {'form': form, 'data': model_object})
