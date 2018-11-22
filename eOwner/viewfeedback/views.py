from django.shortcuts import render, redirect
from feedback.models import Feedback


def feed(request):

    model_object1 = Feedback.objects.all()

    return render(request, "viewfeedback/viewfeedback.html", {'data': model_object1})

