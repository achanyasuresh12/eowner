from django.conf.urls import url
from .views import busses

app_name = 'viewbus'

urlpatterns = [
    url(r'^$', busses, name='viewbuses_forms'),
]
