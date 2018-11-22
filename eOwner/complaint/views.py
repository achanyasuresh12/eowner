from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Complaint


def comp(request):
    login_id = request.session['logid']
    model_object = Complaint.objects.filter(user_id=login_id)

    if request.method == 'POST':
        form = forms.complaint_forms(request.POST, request.FILES)
        if form.is_valid():
            complaintObj = form.cleaned_data
            content = complaintObj['complaintcontent']
            bus_id = complaintObj['bus_id']
            a = Complaint(complaintcontent=content, bus_id=bus_id, user_id=login_id)
            a.save()
            return redirect('complaint:complaint_forms')
    else:
        form = forms.complaint_forms

    return render(request, "complaint/complaint.html", {'form': form, 'data': model_object})


def edit_complaint(request, pk):
    login_id = request.session['logid']
    model_objects = Complaint.objects.filter(user_id=login_id)
    template = 'complaint/complaint.html'
    post = get_object_or_404(Complaint, pk=pk)

    if request.method == 'POST':
        form = forms.complaint_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('complaint:complaint_forms')
    else:
            form = forms.complaint_forms(instance=post)
            context = {
                'form': form,
                'post': post,
                'data': model_objects,
            }
    return render(request, template, context)


def delete_complaint(request, pk):
    post = get_object_or_404(Complaint, pk=pk)
    post.delete()
    return redirect('complaint:complaint_forms')
