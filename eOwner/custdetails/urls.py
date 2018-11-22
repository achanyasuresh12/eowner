from django.conf.urls import url
from .views import custo

app_name = 'custdetails'

urlpatterns = [
    url(r'^$', custo, name='custdetails_forms'),

]
