from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Businfo


def businf(request):
    login_id = request.session['logid']
    model_object = Businfo.objects.filter(mgr_id=login_id)

    if request.method == 'POST':
        form = forms.businfo_forms(request.POST, request.FILES)
        if form.is_valid():
            busObj = form.cleaned_data
            name = busObj['name']
            dropping_points = busObj['dropping_points']
            a = Businfo(name=name, dropping_points=dropping_points, mgr_id=login_id)
            a.save()
            return redirect('businfo:businfo_forms')
    else:
        form = forms.businfo_forms

    return render(request, "businfo/businfo.html", {'form': form, 'data': model_object})


def edit_businfo(request, pk):
    login_id = request.session['logid']
    model_objects = Businfo.objects.filter(mgr_id=login_id)
    template = 'businfo/businfo.html'
    post = get_object_or_404(Businfo, pk=pk)

    if request.method == 'POST':
        form = forms.businfo_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('businfo:businfo_forms')
    else:
        form = forms.businfo_forms(instance=post)
        context = {
                'form': form,
                'post': post,
                'data': model_objects,
            }
    return render(request, template, context)


def delete_businfo(request, pk):
    post = get_object_or_404(Businfo, pk=pk)
    post.delete()
    return redirect('businfo:businfo_forms')


# Create your views here.
