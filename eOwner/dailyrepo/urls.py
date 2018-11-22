from django.conf.urls import url
from .views import dailyrep, edit_dailyrep, delete_dailyrep

app_name = 'dailyrepo'

urlpatterns = [
    url(r'^$', dailyrep, name='dailyreports_forms'),
    url(r'^edit_dailyrep/(?P<pk>\d+)/$', edit_dailyrep, name='edit_dailyrep'),
    url(r'^delete_dailyrep/(?P<pk>\d+)/$', delete_dailyrep, name='delete_dailyrep'),
]
