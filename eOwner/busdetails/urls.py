from django.conf.urls import url
from .views import busdet, edit_busdetails, delete_busdetails

app_name = 'busdetails'

urlpatterns = [
    url(r'^$', busdet, name='busdetails_forms'),
    url(r'^edit_busdetails/(?P<pk>\d+)/$', edit_busdetails, name='edit_busdetails'),
    url(r'^delete_busdetails/(?P<pk>\d+)/$', delete_busdetails, name='delete_busdetails'),
]
