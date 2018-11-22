from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Busdetails


def busdet(request):
    login_id = request.session['logid']
    model_object = Busdetails.objects.filter(mgr_id=login_id)

    if request.method == 'POST':
        form = forms.busdetails_forms(request.POST, request.FILES)
        if form.is_valid():
            busObj = form.cleaned_data
            name = busObj['name']
            registno = busObj['regno']
            permitno = busObj['permitno']
            seat = busObj['seat']
            source = busObj['source']
            destination = busObj['destination']
            description = busObj['description']
            arrival_time = busObj['arrival_time']
            departure_time =busObj['departure_time']
            seatorder = busObj['seatorder']
            a = Busdetails(name=name, regno=registno, permitno=permitno, seat=seat, source=source, destination=destination, description=description, arrival_time=arrival_time, departure_time=departure_time,seatorder=seatorder, mgr_id=login_id)
            a.save()
            return redirect('busdetails:busdetails_forms')
    else:
        form = forms.busdetails_forms

    return render(request, "busdetails/busdetails.html", {'form': form, 'data': model_object})


def edit_busdetails(request, pk):
    login_id = request.session['logid']
    model_objects = Busdetails.objects.filter(mgr_id=login_id)
    template = 'busdetails/busdetails.html'
    post = get_object_or_404(Busdetails, pk=pk)

    if request.method == 'POST':
        form = forms.busdetails_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('busdetails:busdetails_forms')
    else:
        form = forms.busdetails_forms(instance=post)
        context = {
                'form': form,
                'post': post,
                'data': model_objects,
            }
    return render(request, template, context)


def delete_busdetails(request, pk):
    post = get_object_or_404(Busdetails, pk=pk)
    post.delete()
    return redirect('busdetails:busdetails_forms')
