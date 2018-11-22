from django.conf.urls import url
from .views import nets

app_name = 'net'

urlpatterns = [
    url(r'^$', nets, name='net'),
]
