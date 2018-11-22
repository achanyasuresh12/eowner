from django.shortcuts import render, redirect
from . import forms
from users.models import User


def userhome(request):
    return render(request, 'userhomepage/userhomepage.html', {'logid': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.login_forms(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            if User.objects.filter(psgusername=username).exists() and User.objects.filter(
                    psgpassword=password).exists():
                obj = User.objects.get(psgusername=username)

                request.session['logid'] = obj.id
                return redirect('userlogin:userhome')
            else:
                return render(request, 'userlogin/userlogin.html', {'form': form})
    else:
        form = forms.login_forms()
    return render(request, 'userlogin/userlogin.html', {'form': form})
