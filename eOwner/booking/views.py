from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Ticketbooking


def book(request):
    login_id = request.session['logid']
    model_object = Ticketbooking.objects.filter(user_id=login_id)

    if request.method == 'POST':

        form = forms.booking_forms(request.POST, request.FILES)
        if form.is_valid():
            bookkObj = form.cleaned_data
            date = bookkObj['date']
            source = bookkObj['source']
            destination = bookkObj['destination']
            seat = bookkObj['seat']
            bus_id = bookkObj['bus_id']
            duration = bookkObj['duration']
            dropping_points = bookkObj['dropping_points']
            fare = bookkObj['fare']
            a = Ticketbooking(date=date, source=source, destination=destination, seat=seat, bus_id=bus_id, duration=duration, dropping_points=dropping_points, fare=fare, user_id=login_id)
            a.save()

            return redirect('booking:booking_forms')
    else:
        form = forms.booking_forms

    return render(request, "bookseat/bookseat.html", {'form': form, 'data': model_object})


def edit_book(request, pk):
    login_id = request.session['logid']
    model_objects = Ticketbooking.objects.filter(user_id=login_id)
    template = 'bookseat/bookseat.html'
    post = get_object_or_404(Ticketbooking, pk=pk)

    if request.method == 'POST':
        form = forms.booking_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('booking:booking_forms')
    else:
            form = forms.booking_forms(instance=post)
            context = {
                'form': form,
                'post': post,
                'data': model_objects,
            }
    return render(request, template, context)


def delete_book(request, pk):
    post = get_object_or_404(Ticketbooking, pk=pk)
    post.delete()
    return redirect('booking:booking_forms')
