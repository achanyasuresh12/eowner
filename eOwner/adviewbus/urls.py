from django.conf.urls import url
from .views import admbus

app_name = 'adviewbus'

urlpatterns = [
    url(r'^$', admbus, name='adviewbusdet_forms'),
]
