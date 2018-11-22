from django.conf.urls import url
from .views import viewseat, verify_details

app_name = 'viewseatdetails'

urlpatterns = [
    url(r'^$', viewseat, name='viewseatdet_forms'),
    url(r'^verify_details/(?P<pk>\d+)$', verify_details, name='verify_details'),

]
