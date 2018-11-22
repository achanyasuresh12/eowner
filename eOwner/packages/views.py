from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Packages


def packg(request):
    login_id = request.session['logid']
    model_object = Packages.objects.filter(mgr_id=login_id)

    if request.method == 'POST':
        form = forms.packages_forms(request.POST, request.FILES)
        if form.is_valid():
            packgObj = form.cleaned_data
            name = packgObj['name']
            duration = packgObj['duration']
            seatcount = packgObj['seatcount']
            rate = packgObj['rate']
            description = packgObj['description']
            a = Packages(name=name, duration=duration, seatcount=seatcount, rate=rate, description=description, mgr_id=login_id)
            a.save()
            return redirect('packages:packages_forms')
    else:
        form = forms.packages_forms

    return render(request, "packages/packages.html", {'form': form, 'data': model_object})


def edit_packg(request, pk):
    login_id = request.session['logid']
    model_objects = Packages.objects.filter(mgr_id=login_id)
    template = 'packages/packages.html'
    post = get_object_or_404(Packages, pk=pk)

    if request.method == 'POST':
        form = forms.packages_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('packages:packages_forms')
    else:
        form = forms.packages_forms(instance=post)
        context = {
                 'form': form,
                 'post': post,
                 'data': model_objects,
            }
    return render(request, template, context)


def delete_packg(request, pk):
    post = get_object_or_404(Packages, pk=pk)
    post.delete()
    return redirect('packages:packages_forms')
