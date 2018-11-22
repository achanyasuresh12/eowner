from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import State


def state(request):
    login_id = request.session['logid']
    model_object = State.objects.filter(mgr_id=login_id)

    if request.method == 'POST':
        form = forms.state_forms(request.POST, request.FILES)
        if form.is_valid():
            busObj = form.cleaned_data
            state_name = busObj['state_name']
            a = State(state_name=state_name, mgr_id=login_id)
            a.save()
            return redirect('state:state_forms')
    else:
        form = forms.state_forms

    return render(request, "state/state.html", {'form': form, 'data': model_object})


def edit_state(request, pk):
    login_id = request.session['logid']
    model_objects = State.objects.filter(mgr_id=login_id)
    template = 'state/state.html'
    post = get_object_or_404(State, pk=pk)

    if request.method == 'POST':
        form = forms.state_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('state:state_forms')
    else:
        form = forms.state_forms(instance=post)
        context = {
                'form': form,
                'post': post,
                'data': model_objects,
            }
    return render(request, template, context)


def delete_state(request, pk):
    post = get_object_or_404(State, pk=pk)
    post.delete()
    return redirect('state:state_forms')
