from django.shortcuts import render, redirect
from . import forms
from .models import User
# from django.core.mail import EmailMessage


def user(request):

    if request.method == 'POST':
        form = forms.user_forms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return redirect('users:user_forms')
    else:
        form = forms.user_forms

    return render(request, "registration/registration.html", {'form': form})

