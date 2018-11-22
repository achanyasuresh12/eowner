from django.shortcuts import render, redirect
from . import forms
from . models import Managers
from django.core.mail import EmailMessage


def manager(request):

    if request.method == 'POST':
        form = forms.manager_forms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            obj = form.cleaned_data
            mail = obj['mgremail']
            uname = obj['mgrusername']
            pwd = obj['mgrpassword']
            instance.save()
            email = EmailMessage('eOwner-Manager Registration', 'Registration Successful username:   '+uname+'   Password:'  +pwd+'', to=[mail])
            email.send()
            return redirect('managers:manager_forms')
    else:
        form = forms.manager_forms

    return render(request, "mgregistration/mgregistration.html", {'form': form})
