from django.conf.urls import url
from .views import feed

app_name = 'viewfeedback'

urlpatterns = [
    url(r'^$', feed, name='viewfeedback_forms'),

]
