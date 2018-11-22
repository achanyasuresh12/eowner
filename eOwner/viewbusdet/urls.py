from django.conf.urls import url
from .views import buss

app_name = 'viewbusdet'

urlpatterns = [
    url(r'^$', buss, name='viewbusdet_forms'),
]
