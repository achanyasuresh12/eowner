from django.shortcuts import render,redirect
from complaint.models import Complaint


def compp(request):
    login_id = request.session['logid']

    model_object1 = Complaint.objects.all()

    return render(request, "viewcomplaint/Viewcomplaint.html", {'data': model_object1})

