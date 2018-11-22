
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Feedback


def fed(request):
    login_id = request.session['logid']
    model_object = Feedback.objects.filter(user_id=login_id)

    if request.method == 'POST':

        form = forms.feedback_forms(request.POST, request.FILES)
        if form.is_valid():
            feedbackObj = form.cleaned_data
            content = feedbackObj['feedbackcontent']
            bus_id = feedbackObj['bus_id']
            a = Feedback(feedbackcontent=content, bus_id=bus_id, user_id=login_id)
            a.save()

            return redirect('feedback:feedback_forms')
    else:
        form = forms.feedback_forms

    return render(request, "feedback/feedback.html", {'form': form, 'data': model_object})


def edit_feedback(request, pk):
    login_id = request.session['logid']
    model_objects = Feedback.objects.filter(user_id=login_id)
    template = 'feedback/feedback.html'
    post = get_object_or_404(Feedback, pk=pk)

    if request.method == 'POST':
        form = forms.feedback_forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('feedback:feedback_forms')
    else:
            form = forms.feedback_forms(instance=post)
            context = {
                'form': form,
                'post': post,
                'data': model_objects,
            }
    return render(request, template, context)


def delete_feedback(request, pk):
    post = get_object_or_404(Feedback, pk=pk)
    post.delete()
    return redirect('feedback:feedback_forms')






