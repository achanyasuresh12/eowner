from django.shortcuts import render, redirect
from . import forms
from managers.models import Managers


def managerhome(request):
    return render(request, 'managerhomepage/managerhome.html', {'logid': request.session['logid']})


def mgrlogin(request):
    if request.method == 'POST':
        form = forms.managerlogin_form(request.POST)
        if form.is_valid():
            mgrObj = form.cleaned_data
            username = mgrObj['username']
            password = mgrObj['password']
            if Managers.objects.filter(mgrusername=username).exists() and Managers.objects.filter(mgrpassword=password).exists():
                obj = Managers.objects.get(mgrusername=username)

                request.session['logid'] = obj.id
                return redirect('managerlogin:managerhome')
            else:
                return render(request, 'managerloginpage/managerlogin.html', {'form': form})
    else:
        form = forms.managerlogin_form()
    return render(request, 'managerloginpage/managerlogin.html', {'form': form})

# Create your views here.
